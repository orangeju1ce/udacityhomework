# udacityhomework
quizzes and stuff
def nextDay(year, month, day):
    if day < monthcheck(month, year): #modified if statement, uses monthcheck to return amount of days 
        return year, month, day + 1   #that are necessary for nextday function
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def leapcheck(year):
    if year%4==0: #divides year by 4, if there is no remainder, returns True for leap year
        return True
    return False

def monthcheck(month, year):
    """checks the month, checks leap year, returns appropriate month and days"""
    if month == 2:
        if leapcheck(year) == True: #returns 29 if leap year, 28 if not leap year for february
            return 29
        return 28
    if month == 9 or month == 4 or month == 6 or month == 11: #april, june, september, and november, returns 30 days
        return 30
    return 31 #all others have 31 days


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days



def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
