from datetime import datetime, date
import time

current_time = datetime.now()
time.sleep(1)
print(current_time)

# TO AVOID THE MILLISECONDS 
formated_time = current_time.strptime("%Y-%m-%d %H:%M:%S")     
print(formated_time)


current_time2 = date.today().year
time.sleep(2)
print(current_time2)

# current_time3 = date.today().weekday
# time.sleep(3)
# print(current_time3)


event_date = datetime(2025, 12, 9, 0, 0)
print (event_date)

# CALCULATE TIME DIFFERENCES 
event_date = datetime(2025, 12, 9, 0, 0)
current_time = datetime.now()
time_difference = event_date - current_time
print (f"Days remaining: {time_difference.days} days")

