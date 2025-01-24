from datetime import datetime, date, timedelta
now = datetime.now()
# now = datetime.now()
# print("Current Date and Time:", now)

# 1. datetime Module


# today = date.today()
# print("Current Date:", today)




# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted Date:", formatted_date)

# current_date = date.today()
# formatted_date = current_date.strftime("%B %d, %Y")
# print("Formatted Current Date:", formatted_date)




# date_string = "2025-01-23"
# parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
# print("Parsed Date:", parsed_date)




# now = datetime.now()
# future_date = now + timedelta(days=10)
# print("Future Date (10 days ahead):", future_date)
# past_date = now - timedelta(days=5)
# print("Past Date (5 days ago):", past_date)



# now = datetime.now()
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second
# print("Date Components:", year, month, day, hour, minute, second)
# print("Year:", year)
# print("Month:", month)
# print("Day:", day)
# print("Hour:", hour)
# print("Minute:", minute)
# print("Second:", second)




# now = datetime.now()
# new_date = now.replace(year=2030, month=12, day=25)
# print("Modified Date:", new_date)




# date1 = datetime(2025, 1, 23)
# date2 = datetime(2024, 12, 25)
# difference = date1 - date2
# print("Difference Between Dates:", difference.days, "days")




# iso_date = now.isoformat()
# print("ISO Format Date:", iso_date)




# specific_date = datetime(2023, 12, 31, 23, 59, 59)
# print("Specific Date:", specific_date)



# 2. time Module
import time
timestamp = time.time()

# timestamp = time.time()
# print("Current Timestamp:", timestamp)




# readable_time = time.ctime(timestamp)
# print("Readable Time:", readable_time)




# print("Sleeping for 2 seconds...")
# time.sleep(2)
# print("Awake now!")




# gmt_time = time.gmtime()
# local_time = time.localtime()
# print("GMT Time:", time.asctime(gmt_time))
# print("Local Time:", time.asctime(local_time))




# start_time = time.time()
# time.sleep(2)
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution Time: {execution_time} seconds")




# process_time = time.process_time()                                         # --
# print("Process Time:", process_time)




# 3. calendar Module
import calendar

# is_leap = calendar.isleap(2024)
# print("Is 2024 a Leap Year?:", is_leap)




# print("January 2025 Calendar:")
# print(calendar.month(2025, 1))

# year = 2025
# month = 1
# print(calendar.month(year, month))




# first_weekday, days_in_month = calendar.monthrange(2025, 1)
# print("First Weekday and Days in January 2025:", first_weekday, days_in_month)



# year_calendar = calendar.TextCalendar().formatyear(2025)
# print("Year Calendar for 2025:")
# print(year_calendar)




# print("Days in January 2025:")
# for day in calendar.Calendar().itermonthdays(2025, 1):
#     print(day, end=" ")
# print()



# 4. pytz Module
# import pytz
#
# utc_now = datetime.now(pytz.utc)
# timezone = pytz.timezone("America/New_York")
# new_york_time = utc_now.astimezone(timezone)
# print("New York Time:", new_york_time)
#



# print("First 10 Timezones:")
# for tz in pytz.all_timezones[:10]:
#     print(tz)




# 5. dateutil Module
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

# new_date = now + relativedelta(weeks=1, years=2)
# print("Date After Adding 1 Week and 2 Years:", new_date)




# date = parse("January 23, 2025")
# print("Parsed Arbitrary Date String:", date)




# date_with_tz = parse("2025-01-23 10:00:00+05:30")
# print("Parsed Date with Timezone:", date_with_tz)




# 6. strftime and strptime Examples

# formatted_date = now.strftime("%A, %B %d, %Y - %I:%M %p")
# print("Formatted Date (Custom):", formatted_date)




# date_string = "23-01-2025 10:15:30"
# date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
# print("Parsed Custom Format Date:", date)

# import datetime
# datetime.datetime.today()
# date1=datetime.datetime(2025, 1, 23)
# datetime.datetime.today().weekday()


# start_date = datetime(2025,1,1)
# end_date = datetime(2025,1,10)
#
# delta = timedelta(days=1)
#
# dates = []
#
# while start_date <= end_date:
#     dates.append(start_date.isoformat())
#     start_date += delta
#
# print(dates)



# def dates_range(start,end):
#     delta = end - start
#     days = [start + timedelta(days=i)
#             for i in range(delta.days + 1)]
#     return days
#
# start= datetime(2025,1,1)
# end= datetime(2025,1,10)
#
# daterange=dates_range(start,end)
# print(daterange)

# from datetime import timedelta, date
#
# def daterange(start, end):
#   return [start + timedelta(n) for n in range(int((end - start).days))]
# start= datetime(2025,1,1)
# end= datetime(2025,1,10)
# date_range=daterange(start,end)
# print(date_range)

#
# from datetime import date
# date_to_check = "2025-01-25"
# is_weekend(date(2025, 1, 25))
# # is_weekend(date(2020, 10, 28))





from datetime import datetime

# Define the future date
future_date = datetime(2025, 12, 25)

# Get the current date
current_date = datetime.now()

days_until = (future_date - current_date).days

# Output the result
print(f"Number of days until {future_date.date()}: {days_until}")


import calendar
month = calendar.monthrange(2025, 2)[1]
print(month)


from datetime import date, timedelta
date1 = date(2023, 1, 1)
print(date1)
date2 = date1 + timedelta(days=100)
print (date2)



from datetime import datetime

birth_date = datetime(1990, 5, 15)
current_date = datetime.now()
age = current_date.year - birth_date.year
# if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
#     age =age-1
print("Your age is:", age)






from datetime import datetime, timedelta

given_date = datetime(2023, 1, 1)
new_date = given_date + timedelta(days=100)

print("Given date:", given_date)
print("Date after 100 days:", new_date)





import time

start_time = time.time()
time.sleep(1)
end_time = time.time()
execution_time = end_time - start_time
print(f"{execution_time:.2f} seconds")
# .2f indicates that the number should be formatted as a floating-point number (f) with two digits after the decimal point (.2)

import time

start_time = time.time()
time.sleep(1)
end_time = time.time()
execution_time = end_time - start_time
print(execution_time ,"seconds")




import time

current_timestamp = time.time()
print(current_timestamp)





import time

def countdown_timer(countdown):
    while countdown > 0:                 # greater than
        print(countdown)
        time.sleep(1)
        countdown = countdown - 1
    print("Time's up!")

countdown_timer(5)
