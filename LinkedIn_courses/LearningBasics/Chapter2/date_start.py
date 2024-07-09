from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():

    today = date.today()
    print("Today's date is", today)

    print("Date components", today.day, today.month, today.year)

    print("Today's weekday # is", today.weekday())
    days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
    print("Which is a ", days[today.weekday()])
    print(today.weekday())
    today = datetime.now()
    print("The current date and time is", today)


if __name__ == "__main__":
    main()

formating dates


def main():
    now = datetime.now()

    print(now.strftime("the current year is: %Y"))
    print(now.strftime("%a, %d %B, %y"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-h time: %H:%M"))


if __name__ == "__main__":
    main()


def main():
    print(timedelta(days=365, hours=5, minutes=1))

    now = datetime.now()
    print("today is", now)

    print("one year from now will be", str(now + timedelta(days=365)))

    print("in 2 weeks and 3 days will be", str(
        now + timedelta(weeks=2, days=3)))

    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("one week ago it was", s)

    today = date.today()
    afd = date(today.year, 4, 1)

    if afd < today:
        print("April's fools' day already went by:", ((today - afd).days))
        afd.replace(year=today.year + 1)

    time_to_afd = afd - today
    print("it is", time_to_afd.days, "days until next April's fools day")


if __name__ == '__main__':
    main()

# working with calendars
import calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2024, 7, 0, 0)
print(str)

hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2024, 7)
print(str)

for i in c.itermonthdays(2024, 8):
    print(i)

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

print("team meatins will be on:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2024, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.WEDNESDAY] != 0:
        meetday = weekone[calendar.WEDNESDAY]
    else:
        meetday = weektwo[calendar.WEDNESDAY]

    print(calendar.month_name[m], meetday)


# challenge exercise
show_expected_result = False
show_hints = False


def count_days(theyear, themonth, whichday):
    import calendar
    daycount = 0
    weekslist = calendar.monthcalendar(theyear, themonth)

    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount


testyear = 2026
testmonth = 12
testday = 0

result = Answer.count_days(testyear, themonth, testday)
