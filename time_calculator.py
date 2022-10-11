def get_current_weekday(n_days):
    if n_days == 1:
        return "(next day)"
    elif n_days > 1:
        return f"({n_days} days later)"
    return ""

def add_time(start, duration, expecting_weekday = False):
    start_hour, start_min = start.split(":")
    start_min, suffix = start_min.split(" ")
    xdays_later = 0

    full_day = 24
    half_day = 12

    # end times
    duration_hr, duration_min = duration.split(":")

    # updated times
    start_hour = int(start_hour)
    start_min = int(start_min) 
    duration_hr = int(duration_hr)
    duration_min = int(duration_min)
    
    # days array
    week_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    
    # total time count
    total_hr = start_hour + duration_hr
    total_min = start_min + duration_min

    # time calculation
    if total_min >= 60:
        total_hr += total_min // 60
        total_min = total_min % 60
    
    if duration_hr or duration_min:
        # AM/PM selection
        # increase day if total_hr >= 24
        if (suffix == 'PM' and total_hr > full_day) and (total_hr % full_day) >= 1:
            xdays_later += 1

        if total_hr >= half_day:
            xdays_later += total_hr // full_day

        # adjusting the suffix
        temp = total_hr
        while True:
            if temp < half_day:
                break

            if suffix == "AM":
                suffix = "PM"
            else:
                suffix = "AM"
            
            temp -= half_day

    # remaining hours and minutes
    hours_left = total_hr % half_day
    mins_left = total_min % 60
        
    # preparing the output
    new_time = f"{hours_left}:{mins_left:02} {suffix}"

    if expecting_weekday is not False:
        weekday = expecting_weekday.strip().lower()
        current_day_index = (week_days.index(weekday) + xdays_later) % 7
        current_day = week_days[current_day_index]
        new_time += f", {current_day} {get_current_weekday(xdays_later)}"

    return new_time

print(add_time("10:10 PM", "3:30", "Monday"))
