# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def leapyear(year):
    if year%4 == 0:
        return 366
    return 365

def daysinyears(year):
    leap = 0
    start = 1
    normal = 0
    while start <= year:
        if start%400 == 0:
            start = start +1
            leap = leap +1
        if start%100 == 0:
            normal = normal +1
            start = start+1
        if start%4 == 0:
            start = start +1
            leap = leap +1
        else: 
            normal = normal +1
            start = start +1

    return normal*360+ leap*361
    
print daysinyears(4)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    birthday = daysinyears(year1) + (month1-1)*30 +day1
    current = daysinyears(year2) + (month2-1)*30 +day2
    return current - birthday

print daysBetweenDates(2012,1,1,2013,1,1)

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
    
