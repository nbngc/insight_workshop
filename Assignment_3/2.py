# Write an if statement to determine whether a variable holding a year is a leap year.

def checkleapyear(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year =5000
if checkleapyear(year):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))