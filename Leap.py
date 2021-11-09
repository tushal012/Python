''' 
@Author : Tushal kumar
@Date : 2021-11-07
@Tittle :   To check the input year is leap  year or not 
'''

 
def checkYear(year):
    
    
    # Return true if year is a multiple
    # of 4 and not multiple of 100.
    # OR year is multiple of 400.
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));
 

year = int(input("Enter a Year:"))
if(checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")