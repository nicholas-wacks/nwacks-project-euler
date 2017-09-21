daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

sum = 0
dayOfWeek = 2
for year in range(1, 101):
    for month in range(12):
        if (dayOfWeek == 0):
            sum += 1

        dayOfWeek += daysInMonth[month]
        if (month == 1 and year % 4 == 0):
            dayOfWeek += 1

        dayOfWeek = dayOfWeek % 7

print(sum)
            