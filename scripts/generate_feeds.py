import os
import sys
import datetime

def get_rolling_window():
    today = datetime.date.today()
    
    # Start Date: 1st day of the previous month
    first_of_this_month = datetime.date(today.year, today.month, 1)
    prev_month_last_day = first_of_this_month - datetime.timedelta(days=1)
    start_date = datetime.date(prev_month_last_day.year, prev_month_last_day.month, 1)
    
    # End Date: last day of the month 12 months after the current month
    # Target month: same month next year
    target_year = today.year + 1
    target_month = today.month
    
    if target_month == 12:
        next_month_first = datetime.date(target_year + 1, 1, 1)
    else:
        next_month_first = datetime.date(target_year, target_month + 1, 1)
    end_date = next_month_first - datetime.timedelta(days=1)
    
    return start_date, end_date

def parse_event_date(dt_line):
    # Extracts the date from a DTSTART line
    # Examples:
    # "DTSTART;VALUE=DATE:20710316" -> date(2071, 3, 16)
    # "DTSTART:20710316T120000Z" -> date(2071, 3, 16)
    val = dt_line.split(':')[-1].strip()
    if len(val) >= 8:
        try:
            year = int(val[0:4])
            month = int(val[4:6])
            day = int(val[6:8])
            return datetime.date(year, month, day)
        except ValueError:
            return None
    return None

def filter_ics(source_path, target_path, start_date, end_date):
    if not os.path.exists(source_path):
        print(f"Error: Source file {source_path} does not exist.")
        return False
        
    print(f"Processing {source_path}...")
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.splitlines()
    
    header = []
    events = []
    footer = []
    
    in_event = False
    current_event_lines = []
    current_event_date = None
    
    for line in lines:
        if line.startswith('BEGIN:VEVENT'):
            in_event = True
            current_event_lines = [line]
            current_event_date = None
        elif line.startswith('END:VEVENT'):
            current_event_lines.append(line)
            if current_event_date and start_date <= current_event_date <= end_date:
                events.append("\n".join(current_event_lines))
            in_event = False
        elif in_event:
            current_event_lines.append(line)
            if line.startswith('DTSTART'):
                current_event_date = parse_event_date(line)
        else:
            if not events:
                header.append(line)
            else:
                footer.append(line)
                
    # Reassemble and write to target path
    new_content = "\n".join(header) + "\n" + "\n".join(events) + "\n" + "\n".join(footer) + "\n"
    
    # Ensure directories exist
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    with open(target_path, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(new_content)
        
    print(f"Successfully generated {target_path} (Events count: {len(events)})")
    return True

def main():
    start_date, end_date = get_rolling_window()
    print(f"Rolling time window: {start_date.isoformat()} to {end_date.isoformat()}")
    
    # Define file mapping (source -> target)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    mapping = {
        os.path.join(base_dir, "sources", "chuyi-shiwu-simplified-all.ics"): os.path.join(base_dir, "chuyi-shiwu-simplified.ics"),
        os.path.join(base_dir, "sources", "chuyi-shiwu-traditional-all.ics"): os.path.join(base_dir, "chuyi-shiwu-traditional.ics")
    }
    
    success = True
    for src, tgt in mapping.items():
        if not filter_ics(src, tgt, start_date, end_date):
            success = False
            
    if not success:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
