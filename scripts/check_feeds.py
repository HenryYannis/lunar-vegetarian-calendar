"""生成后自检：订阅文件有问题就让 job 失败，避免把坏文件推给所有订阅者。

检查项：
- 文件以 BEGIN:VCALENDAR 开头、END:VCALENDAR 结尾，VEVENT 成对出现
- 事件数在合理范围内（13~14 个月窗口，正常 26~30 个）
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
    with open(path, encoding="utf-8", newline="") as f:
        raw = f.read()
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
