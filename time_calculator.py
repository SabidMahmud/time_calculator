def get_days_later(days):
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"
    return ""


def add_time(start_time, end_time, day=False):
    
    # constants
    HOURS_IN_ONE_DAY = 24
    HOURS_IN_HALF_DAY = 12
    WEEK_DAYS = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]


    days_later = 0
    hours, mins = start_time.split(":")
    mins, period = mins.split(" ")
    end_time_hrs, end_time_mins = end_time.split(":")

    hours = int(hours)  # start time  hours
    mins = int(mins)  # start time  minutes
    end_time_hrs = int(end_time_hrs)  # end time hours
    end_time_mins = int(end_time_mins)  # end time minutes
    period = period.strip().lower()  # AM or PM

    total_mins = mins + end_time_mins
    total_hours = hours + end_time_hrs

    if total_mins >= 60:
        total_hours += int(total_mins / 60)
        total_mins = int(total_mins % 60)

    if end_time_hrs or end_time_mins:
        if period == "pm" and total_hours > HOURS_IN_HALF_DAY:
            if total_hours % HOURS_IN_ONE_DAY >= 1.0:
                days_later += 1

        if total_hours >= HOURS_IN_HALF_DAY:
            hours_left = total_hours / HOURS_IN_ONE_DAY
            days_later += int(hours_left)

        temp_hours = total_hours
        while True:
            if temp_hours < HOURS_IN_HALF_DAY:
                break
            if period == "am":
                period = "pm"
            else:
                period = "am"
            temp_hours -= HOURS_IN_HALF_DAY

    remaining_hours = int(total_hours % HOURS_IN_HALF_DAY) or hours + 1
    remaining_mins = int(total_mins % 60)

    results = f"{remaining_hours}:{remaining_mins:02} {period.upper()}"
    if day:  # add the day of the week
        day = day.strip().lower()
        selected_day = int((WEEK_DAYS.index(day) + days_later) % 7)
        current_day = WEEK_DAYS[selected_day]
        results += f", {current_day.title()} {get_days_later(days_later)}"

    else:
        results = " ".join((results, get_days_later(days_later)))

    return results.strip()