def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # is leap year
            else:
                return False  # is not lear year
        else:
            return True  # is leap year
    else:
        return False  # is not lear year


def days_in_month(input_year, input_month):
    """ Take the year and month and spit out the days in the month """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(input_year) and input_month == 2:
        return 29
    return month_days[input_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

days_in_month