"""生成后自检：订阅文件有问题就让 job 失败，避免把坏文件推给所有订阅者。

检查项：
- 文件以 BEGIN:VCALENDAR 开头、END:VCALENDAR 结尾，VEVENT 成对出现
- 所有换行都是 CRLF（没有裸 LF / 裸 CR），文件以 CRLF 结尾（RFC 5545 3.1）
- 每一行不超过 75 个 UTF-8 字节（RFC 5545 3.1，超长行必须折叠）
- 每个 VEVENT 都有且只有一个 DTSTAMP 和 UID（RFC 5545 3.6.1）
- 事件数在合理范围内（14 个月窗口，正常 27~30 个）
- 所有日期都落在 generate_feeds.py 的滚动窗口内，且 UID 不重复
- 如果装了 tyme4py（requirements.txt），再逐个核对确实是农历初一或十五
"""
import os
import re
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_feeds import get_rolling_window  # noqa: E402

MIN_EVENTS = 20
MAX_EVENTS = 32
FEEDS = ["chuyi-shiwu-simplified.ics", "chuyi-shiwu-traditional.ics"]


def check(path, start_date, end_date):
    errors = []
    with open(path, "rb") as f:
        data = f.read()

    # 字节层面的检查：换行符和行长度
    if not data.endswith(b"\r\n"):
        errors.append("文件没有以 CRLF 结尾")
    bare_lf = data.count(b"\n") - data.count(b"\r\n")
    bare_cr = data.count(b"\r") - data.count(b"\r\n")
    if bare_lf or bare_cr:
        errors.append(f"有 {bare_lf} 个裸 LF、{bare_cr} 个裸 CR，换行必须是 CRLF")
    physical = data.split(b"\r\n")
    if physical and physical[-1] == b"":
        physical.pop()
    too_long = [i + 1 for i, line in enumerate(physical) if len(line) > 75]
    if too_long:
        errors.append(f"有 {len(too_long)} 行超过 75 字节（未折叠），例如第 {too_long[0]} 行")

    raw = data.decode("utf-8")
    # 先展开折叠行（CRLF 后跟空格或制表符），后面按逻辑行检查
    raw = re.sub(r"\r\n[ \t]", "", raw)
    lines = raw.splitlines()
    if not lines or lines[0] != "BEGIN:VCALENDAR":
        errors.append("第一行不是 BEGIN:VCALENDAR")
    if not lines or lines[-1] != "END:VCALENDAR":
        errors.append("最后一行不是 END:VCALENDAR")
    if raw.count("BEGIN:VEVENT") != raw.count("END:VEVENT"):
        errors.append("BEGIN:VEVENT 与 END:VEVENT 数量不一致")

    dates = []
    for m in re.finditer(r"^DTSTART;VALUE=DATE:(\d{8})\r?$", raw, re.M):
        dates.append(datetime.datetime.strptime(m.group(1), "%Y%m%d").date())
    if not MIN_EVENTS <= len(dates) <= MAX_EVENTS:
        errors.append(f"事件数 {len(dates)} 不在 {MIN_EVENTS}~{MAX_EVENTS} 之间")
    if len(dates) != raw.count("BEGIN:VEVENT"):
        errors.append("有事件缺少 DTSTART;VALUE=DATE")
    outside = [d for d in dates if not start_date <= d <= end_date]
    if outside:
        errors.append(f"有 {len(outside)} 个事件不在窗口内，例如 {outside[0]}")
    uids = re.findall(r"^UID:(.+?)\r?$", raw, re.M)
    if len(uids) != len(set(uids)):
        errors.append("UID 有重复")

    # 每个 VEVENT 必须各有一个 DTSTAMP 和 UID（VALARM 里不会出现这两个属性）
    for i, body in enumerate(re.findall(r"^BEGIN:VEVENT\r?$(.*?)^END:VEVENT\r?$", raw, re.M | re.S), 1):
        for prop in ("DTSTAMP", "UID"):
            n = len(re.findall(rf"^{prop}[:;]", body, re.M))
            if n != 1:
                errors.append(f"第 {i} 个 VEVENT 有 {n} 个 {prop}，应为 1 个")
                break

    try:
        from tyme4py.solar import SolarDay
    except ImportError:
        print("  （未安装 tyme4py，跳过农历日期核对）")
    else:
        for d in dates:
            name = SolarDay.from_ymd(d.year, d.month, d.day).get_lunar_day().get_name()
            if name not in ("初一", "十五"):
                errors.append(f"{d} 是农历{name}，不是初一或十五")
    return len(dates), errors


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    start_date, end_date = get_rolling_window()
    print(f"窗口：{start_date} ~ {end_date}")
    failed = False
    for name in FEEDS:
        count, errors = check(os.path.join(base_dir, name), start_date, end_date)
        if errors:
            failed = True
            print(f"❌ {name}（{count} 个事件）")
            for e in errors:
                print(f"   - {e}")
        else:
            print(f"✅ {name}（{count} 个事件）")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
