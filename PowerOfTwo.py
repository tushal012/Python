''' 
@Author : Tushal kumar
@Date : 2021-11-07
@Tittle :   prints a table of the powers of 2 that are less than or equal to 2^N
'''

'''
@Desc : The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
'''


try:
    power = int(input("Enter A power:"))
    if power >31:
        raise ValueError("Entered A Number Greater Than 31")
    number = 1
    for i in range(power):
        number = number *2
        print(number)

except ValueError: 
    print("Invalid Input")