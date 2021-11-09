''' 
@Author : Tushal Kumar
@Date : 2021-11-07
@Tittle : to find N-th Harmonic Number '''

'''
@desc : Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N

'''
 
# Function to find N-th Harmonic Number
def nthHarmonic(number) :
 
    # H1 = 1
    harmonic = 1.00
 
    # loop to apply the forumula
    # Hn = H1 + H2 + H3 ... +
    # Hn-1 + Hn-1 + 1/n
    for i in range(2, number + 1) :
        harmonic += 1 / i
 
    return harmonic
     
   
if __name__ == "__main__" :
 
    number = int(input("Enter A Number: "))
    print(round(nthHarmonic(number),5))