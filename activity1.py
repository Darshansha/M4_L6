from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("Today is", today)
print("Current time is", now)

print("The year is", today.year)
print("The month is ", today.month)
print("The day is", today.day)