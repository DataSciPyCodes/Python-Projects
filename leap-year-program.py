#Please make sure you execute one METHOD at a time and comment all other METHODS
#Python program to check if year is a leap year or not

#METHOD-1

year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
   
   

#METHOD-2

#Leap Year using Boolean
def check_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter a year : "))
check_year(year)
if check_year(year):
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")
    




#METHOD-3
def check_leap(year):
    if (year%4==0 and year%100!=0 or year%400==0):
        print(year, " is a leap year")
    else:
        print(year, " is not a leap year")

year = int(input("Enter year : "))
check_leap(year)
