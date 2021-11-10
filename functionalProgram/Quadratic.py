''' 
@Author : Tushal kumar
@Date : 2021-11-08
@Tittle :  Write a program Quadratic.py to find the roots of the equation a*x*x + b*x + c.
'''

'''
Desc : (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)
'''

import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# calculate the delta
delta = b*b - 4*a*c

# find two solutions
x = (-b-math.sqrt(delta))/(2*a)
y = (-b+math.sqrt(delta))/(2*a)

print('The solution are {0} and {1}'.format(x,y))
