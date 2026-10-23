import os
import sys
import datetime
import time

def generate_events(start_year, end_year, is_traditional):
    from tyme4py.solar import SolarDay
    
    events = []
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    
    curr = start_date
    # Format current UTC time for DTSTAMP and LAST-MODIFIED
    dtstamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    
    alarm_map = {
        "初一": "明天農曆初一，記得吃素" if is_traditional else "明天农历初一，记得吃素",
        "十五": "明天農曆十五，記得吃素" if is_traditional else "明天农历十五，记得吃素"
    }

    summary_map = {
        "初一": "農曆初一" if is_traditional else "农历初一",
        "十五": "農曆十五" if is_traditional else "农历十五"
    }
    
    total_days = (end_date - start_date).days + 1
    processed = 0
    t0 = time.time()
    
    print(f"Generating {'traditional' if is_traditional else 'simplified'} calendar from {start_year} to {end_year}...")
    
    while curr <= end_date:
        solar = SolarDay.from_ymd(curr.year, curr.month, curr.day)
        lunar = solar.get_lunar_day()
        name = lunar.get_name()
        
        if name in ("初一", "十五"):
            date_str = curr.strftime("%Y%m%d")
            next_day = curr + datetime.timedelta(days=1)
            next_day_str = next_day.strftime("%Y%m%d")
            
            event_summary = summary_map[name]
            
            event = [
                "BEGIN:VEVENT",
                f"DTSTART;VALUE=DATE:{date_str}",
                f"DTEND;VALUE=DATE:{next_day_str}",
                f"DTSTAMP:{dtstamp}",
                f"UID:Ical-lunar-chuyi-shiwu-{date_str}@xbmlz.cn",
                f"CREATED:{dtstamp}",
                f"LAST-MODIFIED:{dtstamp}",
                "SEQUENCE:0",
                "STATUS:CONFIRMED",
                f"SUMMARY:{event_summary}",
                # 初一十五是提醒不是会议，不占用“忙碌”时间
                "TRANSP:TRANSPARENT",
                # 前一天晚上 20:00 提醒（全天事件从当天 0 点往前推 4 小时）
                "BEGIN:VALARM",
                "ACTION:DISPLAY",
                f"DESCRIPTION:{alarm_map[name]}",
                "TRIGGER:-PT4H",
                "END:VALARM",
                "END:VEVENT"
            ]
            events.append("\n".join(event))
            
        curr += datetime.timedelta(days=1)
        processed += 1
        if processed % 50000 == 0:
            pct = (processed / total_days) * 100
            print(f"  Progress: {pct:.1f}% ({processed}/{total_days} days in {time.time()-t0:.1f}s)")
            
    print(f"  Finished: Found {len(events)} events in {time.time()-t0:.1f}s.")
    return events

def write_calendar(path, name, desc, events):
    header = [
        "BEGIN:VCALENDAR",
        "PRODID:-//Lunar Vegetarian Calendar//Generator 1.0//EN",
        "VERSION:2.0",
        "CALSCALE:GREGORIAN",
        f"X-WR-CALNAME:{name}",
        "X-WR-TIMEZONE:Asia/Shanghai",
        f"X-WR-CALDESC:{desc}",
        # 告诉 Apple / Outlook 等客户端每天刷新一次
        "REFRESH-INTERVAL;VALUE=DURATION:P1D",
        "X-PUBLISHED-TTL:P1D",
    ]
    content = "\n".join(header) + "\n" + "\n".join(events) + "\nEND:VCALENDAR\n"
    with open(path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(content)
    print(f"Wrote {name} calendar to {path}")

def main():
    try:
        from tyme4py.solar import SolarDay
    except ImportError:
        print("Error: tyme4py is not installed in the python environment.")
        sys.exit(1)
        
    start_year = 2026
    end_year = 2100
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sources_dir = os.path.join(base_dir, "sources")
    os.makedirs(sources_dir, exist_ok=True)
    
    # 1. Simplified Chinese Version
    write_calendar(
        os.path.join(sources_dir, "chuyi-shiwu-simplified-all.ics"),
        "农历初一十五", "食斋",
        generate_events(start_year, end_year, is_traditional=False),
    )

    # 2. Traditional Chinese Version
    write_calendar(
        os.path.join(sources_dir, "chuyi-shiwu-traditional-all.ics"),
        "農曆初一十五", "食齋",
        generate_events(start_year, end_year, is_traditional=True),
    )

if __name__ == '__main__':
    main()
