''' 
@Author : Tushal kumar
@Date : 2021-11-08
@Tittle :   Write a program WindChill.py that takes two double command-line arguments t
and v and prints the wind 
'''

'''
@Desc : Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour)
'''

import math

try:
        v = float(input("Input wind speed in kilometers/hour: "))
        t = float(input("Input air temperature in degrees Celsius: "))
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (math.pow(v,0.16));
        print("The wind chill index is", int(round(w)))

except Exception as e:
    print(e)
        
