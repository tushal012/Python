#  This program takes a command-line argument N and prints a table of the
# powers of 2 that are less than or equal to 2^N..
def highestPowerof2(n):
 
    res = 0;
    for i in range(n, 0, -1):
         
        # If i is a power of 2
        if ((i & (i - 1)) == 0):
         
            res = i
            break
         
    return res
 

n = 10
print(highestPowerof2(n))