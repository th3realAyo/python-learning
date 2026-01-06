from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
from datetime import timezone



# Fetching the current date
today = datetime.now()
print(today)

# Fetching the current year
print(today.year)

# Fetching the current day
print(today.strftime("%A")) #Returns "Tuesday"
print(today.strftime("%a")) #Returns "Tue"

# Create a date bject
# The datetime() class requires three parameters to create a date: year, month, day.
date_object = datetime(2020, 5, 17)
print(date_object)

print(date_object.strftime("%B"))

#date()
d1 = date(2026, 1, 5)
print(d1)

#time()
t1 = time(14, 30, 0)
print(t1)

#datetime()
dt1 = datetime(2026, 1, 5, 14, 30, 0)
print(dt1)

# timedelta()
delta = timedelta(days=7)
print(delta)


future = datetime.now() + timedelta(days=3)
past = datetime.now() - timedelta(hours=5)
print(f"Future {future} \n Past {past}")


utc = timezone.utc
print(utc)