def calandar(c):
    for i in range (0, len(months)):
        if (c) == months[i]:
            return i + 1

    return p + "is not a planet"

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print (calandar("January"))