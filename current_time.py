import datetime


def current():
    now = datetime.datetime.now()
    print("Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))


def currentyear():
    print("Current year is: ", datetime.date.today().strftime("%Y"))


def currentmonth():
    print("Month of year is: ", datetime.date.today().strftime("%B"))


def week():
    print("Week number of the year is: ", datetime.date.today().strftime("%W"))


def weekday():
    print("Weekday of the week is: ", datetime.date.today().strftime("%w"))


def dayofyear():
    print("Day of year is: ", datetime.date.today().strftime("%j"))


def dayofmonth():
    print("Day of the month is: ", datetime.date.today().strftime("%d"))


def dayofweek():
    print("Day of week is: ", datetime.date.today().strftime("%A"))


current()
currentyear()
currentmonth()
week()
weekday()
dayofyear()
dayofmonth()
dayofweek()
