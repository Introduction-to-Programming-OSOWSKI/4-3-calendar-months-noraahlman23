def calendar(c):
    for i in range (0, len(months)):
        if (c) == months[i]:
            return i + 1

    return p + "is not a month"

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print (calendar("January"))