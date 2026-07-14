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
                "CREATED:19000101T120000Z",
                f"LAST-MODIFIED:{dtstamp}",
                "SEQUENCE:0",
                "STATUS:CONFIRMED",
                f"SUMMARY:{event_summary}",
                "TRANSP:OPAQUE",
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

def main():
    try:
        from tyme4py.solar import SolarDay
    except ImportError:
        print("Error: tyme4py is not installed in the python environment.")
        sys.exit(1)
        
    start_year = 2026
    end_year = 2999
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sources_dir = os.path.join(base_dir, "sources")
    os.makedirs(sources_dir, exist_ok=True)
    
    # 1. Simplified Chinese Version
    simplified_events = generate_events(start_year, end_year, is_traditional=False)
    simplified_header = [
        "BEGIN:VCALENDAR",
        "PRODID:-//Lunar Vegetarian Calendar//Generator 1.0//EN",
        "VERSION:2.0",
        "CALSCALE:GREGORIAN",
        "X-WR-CALNAME:农历初一十五",
        "X-WR-TIMEZONE:Asia/Shanghai",
        "X-WR-CALDESC:食斋",
    ]
    simplified_content = "\n".join(simplified_header) + "\n" + "\n".join(simplified_events) + "\nEND:VCALENDAR\n"
    simplified_path = os.path.join(sources_dir, "chuyi-shiwu-simplified-all.ics")
    with open(simplified_path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(simplified_content)
    print(f"Wrote simplified calendar to {simplified_path}")
    
    # 2. Traditional Chinese Version
    traditional_events = generate_events(start_year, end_year, is_traditional=True)
    traditional_header = [
        "BEGIN:VCALENDAR",
        "PRODID:-//Lunar Vegetarian Calendar//Generator 1.0//EN",
        "VERSION:2.0",
        "CALSCALE:GREGORIAN",
        "X-WR-CALNAME:農曆初一十五",
        "X-WR-TIMEZONE:Asia/Shanghai",
        "X-WR-CALDESC:食齋",
    ]
    traditional_content = "\n".join(traditional_header) + "\n" + "\n".join(traditional_events) + "\nEND:VCALENDAR\n"
    traditional_path = os.path.join(sources_dir, "chuyi-shiwu-traditional-all.ics")
    with open(traditional_path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(traditional_content)
    print(f"Wrote traditional calendar to {traditional_path}")

if __name__ == '__main__':
    main()
