######################################################################
# Starts at the startYear, startMonth, startWeekday (assuming you are starting at the 1st of the month).
# Counts through each month between the time period keeping track of which day of the week the start of
# each month is falling on. Adds to counter if the weekday is a Sunday on the 1st of the month and outputs.
######################################################################

# days in each month for normal and leap years
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthDaysLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# start date information
startYear = 1901
startMonth = 1
startWeekday = 2

# end date information
endYear = 2000
endMonth = 12

# other variables
year = startYear
month = startMonth
weekday = startWeekday

counter = 0

# main
while year < endYear:
    if weekday == 1:
        counter += 1

    if year%4 == 0:
        weekday = (monthDaysLeap[month-1] + weekday)%7
    else:
        weekday = (monthDays[month-1] + weekday)%7
    
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print(counter)
# Solution: 171
    
        



