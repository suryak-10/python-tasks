from datetime import datetime, date, timedelta
import time
import calendar
import pytz
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

# 1. datetime Module

# a. Current Date and Time
now = datetime.now()
print("Current Date and Time:", now)

# b. Current Date
today = date.today()
print("Current Date:", today)

# c. Formatting Dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# d. Parsing Strings into Dates
date_string = "2025-01-23"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed Date:", parsed_date)

# e. Date Arithmetic
future_date = now + timedelta(days=10)
print("Future Date (10 days ahead):", future_date)
past_date = now - timedelta(days=5)
print("Past Date (5 days ago):", past_date)

# f. Extract Components
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print("Date Components:", year, month, day, hour, minute, second)

# g. Replace Specific Components
new_date = now.replace(year=2030, month=12, day=25)
print("Modified Date:", new_date)

# h. Difference Between Two Dates
date1 = datetime(2025, 1, 23)
date2 = datetime(2024, 12, 25)
difference = date1 - date2
print("Difference Between Dates:", difference.days, "days")

# i. Get ISO Format Date
iso_date = now.isoformat()
print("ISO Format Date:", iso_date)

# j. Create a Specific Date
specific_date = datetime(2023, 12, 31, 23, 59, 59)
print("Specific Date:", specific_date)

# 2. time Module

# a. Get Current Time in Seconds
timestamp = time.time()
print("Current Timestamp:", timestamp)

# b. Convert Timestamp to Struct Time
readable_time = time.ctime(timestamp)
print("Readable Time:", readable_time)

# c. Sleep for a Duration
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake now!")

# d. Get GMT and Local Time
gmt_time = time.gmtime()
local_time = time.localtime()
print("GMT Time:", time.asctime(gmt_time))
print("Local Time:", time.asctime(local_time))

# e. Measure Execution Time
start_time = time.time()
time.sleep(2)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")

# f. Get Process Time
process_time = time.process_time()
print("Process Time:", process_time)

# 3. calendar Module

# a. Check If a Year is a Leap Year
is_leap = calendar.isleap(2024)
print("Is 2024 a Leap Year?:", is_leap)

# b. Print a Calendar
print("January 2025 Calendar:")
print(calendar.month(2025, 1))

# c. Month Range
first_weekday, days_in_month = calendar.monthrange(2025, 1)
print("First Weekday and Days in January 2025:", first_weekday, days_in_month)

# d. Generate Year Calendar
year_calendar = calendar.TextCalendar().formatyear(2025)
print("Year Calendar for 2025:")
print(year_calendar)

# e. Iterate Over Month Days
print("Days in January 2025:")
for day in calendar.Calendar().itermonthdays(2025, 1):
    print(day, end=" ")
print()

# 4. pytz Module

# a. Convert to a Specific Timezone
utc_now = datetime.now(pytz.utc)
timezone = pytz.timezone("America/New_York")
new_york_time = utc_now.astimezone(timezone)
print("New York Time:", new_york_time)

# b. List All Timezones                                                     # tz =  "Time Zone"
print("First 10 Timezones:")
for tz in pytz.all_timezones[:10]:
    print(tz)

# 5. dateutil Module

# a. Add Weeks, Days, or Years
new_date = now + relativedelta(weeks=1, years=2)
print("Date After Adding 1 Week and 2 Years:", new_date)

# b. Parse Arbitrary Date Strings
date = parse("January 23, 2025")
print("Parsed Arbitrary Date String:", date)

# c. Parse Date With Timezone
date_with_tz = parse("2025-01-23 10:00:00+05:30")
print("Parsed Date with Timezone:", date_with_tz)

# 6. strftime and strptime Examples

# a. Format Codes for Dates
formatted_date = now.strftime("%A, %B %d, %Y - %I:%M %p")
print("Formatted Date (Custom):", formatted_date)

# b. Parse With Custom Format
date_string = "23-01-2025 10:15:30"
date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
print("Parsed Custom Format Date:", date)