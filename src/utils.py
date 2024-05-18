import time


def determine_rings():
    current_time = time.localtime()
    minutes = current_time.tm_min
    hour = current_time.tm_hour

    if hour > 12:
        hour -= 12

    times = 0
    hour_times = 0

    if minutes == 15:
        times = 1
    elif minutes == 30:
        times = 2
    elif minutes == 45:
        times = 3
    elif minutes == 0:
        times = 4
        hour_times = hour

    return times, hour_times
