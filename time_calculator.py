def add_time(start, duration, expecting_weekday = False):
    start_hour, start_min = start.split(":")
    start_min, suffix = start_min.split(" ")
    days_later = 0

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
    new_hr = start_hour + duration_hr
    new_min = start_min + duration_min

    # time calculation
    if new_min >= 60:
        new_hr += new_min // 60
        new_min = new_min % 60
    
    if duration_hr or duration_min:
        # AM/PM selection
        # increase day if total_hr >= 24
        if (suffix == 'PM' and new_hr > full_day) and (new_hr % full_day) >= 1:
            days_later += 1

        if new_hr >= half_day:
            days_later += new_hr // full_day

        # adjusting the suffix
        temp = new_hr
        while True:
            if temp < half_day:
                break

            if suffix == "AM":
                suffix = "PM"
            else:
                suffix = "AM"
            
            temp -= half_day

    # remaining hours and minutes
    hours_left = new_hr % half_day
    mins_left = new_min % 60
        
    # preparing the output
    final_time = f"{hours_left}:{mins_left:02} {suffix}"

    if expecting_weekday:
        weekday = expecting_weekday.strip().lower()
        current_day_index = (week_days.index(weekday) + days_later) % 7
        current_day = week_days[current_day_index].capitalize()
        final_time += f", {current_day} {get_current_weekday(days_later)}"

    return final_time

def get_current_weekday(n_days):
    if n_days == 1:
        return "(next day)"
    elif n_days > 1:
        return f"({n_days} days later)"
    return ""

print(add_time("10:10 PM", "30:30", "Monday"))
