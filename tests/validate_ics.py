"""用 icalendar 库解析所有 .ics 文件，核对内容（CI 用）。

检查项：
- 根目录两个订阅文件和 sources/ 两个主库都能被 icalendar 正常解析
- 每个事件是全天事件，标题是农历初一/十五（简繁对应），带一个提前 4 小时的提醒
- 主库正好包含 2026-2100 年每一个农历初一和十五（用 requirements.txt 固定的 tyme4py 核对），简繁两份日期一致
- 订阅文件里的事件都来自对应的主库

用法：python tests/validate_ics.py
"""
import datetime
import os
import sys

from icalendar import Calendar
from tyme4py.solar import SolarDay

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIRST_YEAR, LAST_YEAR = 2026, 2100
SUMMARIES = {
    "simplified": {"初一": "农历初一", "十五": "农历十五"},
    "traditional": {"初一": "農曆初一", "十五": "農曆十五"},
}


def load(path):
    with open(path, "rb") as f:
        cal = Calendar.from_ical(f.read())
    events = {}
    errors = []
    for ev in cal.walk("VEVENT"):
        start = ev.decoded("DTSTART")
        if isinstance(start, datetime.datetime) or not isinstance(start, datetime.date):
            errors.append(f"{ev.get('UID')} 不是全天事件")
            continue
        if start in events:
            errors.append(f"{start} 重复")
        alarms = ev.walk("VALARM")
        if len(alarms) != 1 or alarms[0].decoded("TRIGGER") != datetime.timedelta(hours=-4):
            errors.append(f"{start} 的提醒不是一个提前 4 小时的 VALARM")
        events[start] = str(ev.get("SUMMARY"))
    return events, errors


def expected_days():
    days = {}
    d = datetime.date(FIRST_YEAR, 1, 1)
    end = datetime.date(LAST_YEAR, 12, 31)
    while d <= end:
        name = SolarDay.from_ymd(d.year, d.month, d.day).get_lunar_day().get_name()
        if name in ("初一", "十五"):
            days[d] = name
        d += datetime.timedelta(days=1)
    return days


def main():
    expected = expected_days()
    failed = False
    for variant, summaries in SUMMARIES.items():
        source_path = os.path.join("sources", f"chuyi-shiwu-{variant}-all.ics")
        feed_path = f"chuyi-shiwu-{variant}.ics"
        source, errors = load(os.path.join(BASE, source_path))
        if set(source) != set(expected):
            missing = sorted(set(expected) - set(source))
            extra = sorted(set(source) - set(expected))
            errors.append(f"日期与 tyme4py 不一致：缺 {len(missing)} 个，多 {len(extra)} 个")
        for d, summary in source.items():
            if d in expected and summary != summaries[expected[d]]:
                errors.append(f"{d} 标题是「{summary}」，应为「{summaries[expected[d]]}」")
                break
        report(source_path, len(source), errors)
        failed |= bool(errors)

        feed, errors = load(os.path.join(BASE, feed_path))
        stray = [d for d in feed if source.get(d) != feed[d]]
        if stray:
            errors.append(f"有 {len(stray)} 个事件不在主库里，例如 {stray[0]}")
        report(feed_path, len(feed), errors)
        failed |= bool(errors)
    sys.exit(1 if failed else 0)


def report(name, count, errors):
    print(f"{'❌' if errors else '✅'} {name}（{count} 个事件）")
    for e in errors[:10]:
        print(f"   - {e}")


if __name__ == "__main__":
    main()
