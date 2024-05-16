def convert_to_12_hour_format(time):
    
    hours, minutes = map(int, time.split(':'))
    period = "AM" if hours < 12 else "PM"
    hours = hours % 12
    
    if hours == 0:
        hours = 12
        
    return f"{hours:02d}:{minutes:02d} {period}"

t = int(input())
for _ in range(t):
    
    time_24_hour = input().strip()
    print(convert_to_12_hour_format(time_24_hour))