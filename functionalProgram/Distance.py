''' 
@Author : Tushal kumar
@Date : 2021-11-08
@Desc :  Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
'''
import math

try:
    a=input("enter first coordinate : ")
    p1 = a.split(",")

    b=input("enter second coordinate : ")
    p2 = b.split(",")

    distance = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )
    print (distance)

except Exception as e:
        
    print(e)