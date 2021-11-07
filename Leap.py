# to check leap year

 
def checkYear(year):
    number = int(input("Enter a number:"))
 
    # Return true if year is a multiple
    # of 4 and not multiple of 100.
    # OR year is multiple of 400.
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));
 

year = 2020
if(checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")