# Task 1: Get Current Date and Time
# Sample Input: None
# Expected Output: Current date and time in ISO format

from datetime import datetime

current_datetime = datetime.now()
iso_datetime = current_datetime.isoformat()
print(iso_datetime)




# Task 2: Calculate Your Age
# Sample Input: birth_date = datetime(1990, 5, 15)
# Expected Output: Your age in years


from datetime import datetime

birth_date = datetime(1990, 5, 15)
current_date = datetime.now()
age = current_date.year - birth_date.year
print("Your age is:", age)







# Task 3: Add 100 Days to a Given Date
# Sample Input: given_date = datetime(2023, 1, 1)
# Expected Output: Date 100 days after the given date

from datetime import date, timedelta
date1 = date(2023, 1, 1)
date2 = date1 + timedelta(days=100)
print ("100 days after the given date:",date2)






# Task 4: Find the Day of the Week for a Specific Date
# Sample Input: specific_date = datetime(2025, 1, 23)
# Expected Output: "Thursday"

import datetime

Day = datetime.date(year=2025, month=1, day=23).weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[Day])







# Task 5: Convert Local Time to UTC
# Sample Input: timezone = "America/New_York"
# Expected Output: UTC equivalent of the local time

from datetime import datetime
import pytz

timezone = "America/New_York"
local_timezone = pytz.timezone(timezone)
local_time = datetime.now(local_timezone)
utc_time = local_time.astimezone(pytz.utc)

print("Local Time:", local_time)
print("UTC Time:", utc_time)







# Task 6: Find Number of Days in a Month
# Sample Input: year = 2025, month = 2
# Expected Output: 28


import calendar
year = 2025
month = 2
days= calendar.monthrange(year, month)
print(days)





# Task 7: Measure Code Execution Time
# Sample Input: Simulated task duration = 1 second
# Expected Output: Approx. 1 second


import time

start_time = time.time()
time.sleep(1)
end_time = time.time()
execution_time = end_time - start_time
print(f"{execution_time:.2f} seconds")                                             # decimal point (.2)





# Task 8: Parse and Format a Date String
# Sample Input: date_string = "23-01-2025 10:15:30"
# Expected Output: "Thursday, January 23, 2025 at 10:15 AM"

from datetime import datetime

now = datetime.now()
date_string = "23-01-2025 10:15:30"
date1 = now.strftime("%A, %B %d, %Y at 10:15 %p")
print(date1)






# Task 9: Check If a Year is a Leap Year
# Sample Input: year = 2024
# Expected Output: True

is_leap = calendar.isleap(2024)
print( is_leap)






# Task 10: Generate a Calendar for a Specific Year
# Sample Input: year = 2025
# Expected Output: A text calendar of 2025

year_calendar = calendar.TextCalendar().formatyear(2025)
print("Year Calendar for 2025:")
print(year_calendar)






# Task 11: Calculate Days Until a Future Date
# Sample Input: future_date = datetime(2025, 12, 25)
# Expected Output: Number of days until the given date

from datetime import datetime

future_date = datetime(2025, 12, 25)

current_date = datetime.now()

days_until = (future_date - current_date).days

print(f"Number of days until {future_date.date()}: {days_until}")






# Task 12: Get the First and Last Day of a Month
# Sample Input: month = January, year = 2025
# Expected Output: ("2025-01-01", "2025-01-31")



from calendar import monthrange

def get_first_last_day(month, year):
    month_number = datetime.strptime(month, "%B").month

    first_day = f"{year:04d}-{month_number:02d}-01"
    last_day = f"{year:04d}-{month_number:02d}-{monthrange(year, month_number)[1]}"

    return first_day, last_day

month = "January"
year = 2025
print(get_first_last_day(month, year))







# Task 13: Convert a Date to Timestamp
# Sample Input: now
# Expected Output: Timestamp of the current date


import time

current_timestamp = time.time()
print(current_timestamp)





# Task 14: Create a Countdown Timer
# Sample Input: countdown = 5
# Expected Output: Countdown from 5 to "Time's up!"


import time

def countdown_timer(countdown):
    while countdown > 0:
        print(countdown)
        time.sleep(1)
        countdown = countdown - 1
    print("Time's up!")
countdown_timer(5)




# Task 15: Calculate Difference in Hours and Minutes
# Sample Input: date1 = "2025-01-23 08:00", date2 = "2025-01-23 15:30"
# Expected Output: "7 hours and 30 minutes"

# date_with_tz = parse("2025-01-23 08:00+15:30")
# print("Parsed Date with Timezone:", date_with_tz)



from datetime import datetime

date1= "08:00"
date2= "15:30"

time1 = datetime.strptime("08:00", "%H:%M")
(time1.time())

time2 = datetime.strptime("15:30", "%H:%M")
(time2.time())

date= time2 - time1

print(date)





# Task 16: Generate a List of Dates Between Two Dates
# Sample Input: start_date = "2025-01-01", end_date = "2025-01-10"
# Expected Output: List of dates from January 1 to January 10, 2025

from datetime import timedelta

start_date = datetime(2025,1,1)
end_date = datetime(2025,1,10)

date_list = []

while start_date <= end_date:
    date_list.append(start_date)
    start_date += timedelta(days=1)

print(date_list)





# Task 17: Check If a Date is a Weekend
# Sample Input: date_to_check = "2025-01-25"
# Expected Output: True

from datetime import datetime

def is_weekend(date_to_check):
    date_obj = datetime.strptime(date_to_check, "%Y-%m-%d")
    return date_obj.weekday() in [5, 6]

date_to_check = "2025-01-25"
print(is_weekend(date_to_check))







# Task 18: Add Months to a Date
# Sample Input: start_date = "2025-01-15", months_to_add = 6
# Expected Output: "2025-07-15"

from datetime import datetime
from dateutil.relativedelta import relativedelta

date_after_month = datetime(2025,1,15) + relativedelta(months=6)
print(date_after_month.strftime("%Y-%m-%d"))




# Task 19: Get the Current Time in Different Timezones
# Sample Input: Timezones = ["Asia/Kolkata", "Europe/London", "Australia/Sydney"]
# Expected Output: Current time in each specified timezone

from datetime import datetime
import pytz

print("Asia/Kolkata", datetime.now(tz=pytz.timezone("Asia/Kolkata")))
print("Europe/Kyiv", datetime.now(tz=pytz.timezone("Europe/London")))
print("Australia/Sydney", datetime.now(tz=pytz.timezone("Australia/Sydney")))




# Task 20: Find the Quarter of the Year
# Sample Input: Current month = January
# Expected Output: Quarter 1

def quarter(month):
    quarter_dictionary = {
        "Quarter 1" : [1,2,3],
        "Quarter 2" : [4,5,6],
        "Quarter 3" : [7,8,9],
        "Quarter 4" : [10,11,12]
    }

    for key,values in quarter_dictionary.items():
        for value in values:
            if value == month:
                return key

print(quarter(1))