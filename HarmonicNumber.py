''' to find N-th Harmonic Number '''
 
# Function to find N-th Harmonic Number
def nthHarmonic(N) :
 
    # H1 = 1
    harmonic = 1.00
 
    # loop to apply the forumula
    # Hn = H1 + H2 + H3 ... +
    # Hn-1 + Hn-1 + 1/n
    for i in range(2, N + 1) :
        harmonic += 1 / i
 
    return harmonic
     
   
if __name__ == "__main__" :
 
    N = 5
    print(round(nthHarmonic(N),5))