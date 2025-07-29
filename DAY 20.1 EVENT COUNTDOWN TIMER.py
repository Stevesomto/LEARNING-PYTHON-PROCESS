# EVENT COUNTDOWN TIME

from datetime import datetime, timedelta
import time

# GET EVENT DATE AND TIME FROMT HE USER 
def get_event_datetime():
    try:
        date_input = input("Enter the event date (YYYY-MM-DD  HH:MM:SS): ")
        return datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS format.")
        return None

# CALCULATING TIME REMAIN
def calculate_time_remaining(event_date):
    current_datetime = datetime.now()
    time_difference = event_date - current_datetime 
    return time_difference

# DISPLAY THE COUNTDOWN
def display_countdown(time_left):
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\n---- TIME REAMINING :  {days} days, {hours} hours, {minutes} minutes {seconds} second", end="")
    

# MAIN COUNTDOWN LOOP
def start_countdown(event_date):
    while True: 
        time_left = calculate_time_remaining(event_date)
        if time_left.total_seconds() <= 0:
            print("\n Countdown Complete!")
            break
        display_countdown(time_left)
        time.sleep(1)

# MAIN PROGRAMM
event_datetime = get_event_datetime()
if event_datetime:
    print(f"Event set for: {event_datetime}")
    start_countdown(event_datetime)
            
    
        