# program to print prime factors
 
def primeFactors():
    number = int(input("Enter A Number To Find The Prime Factor:"))
    i=2
    prime_factors = []
    while i * i <= number:
        if number % i == 0:
            prime_factors.append(i)
            number//=i
        else:
            i +=1
    if number>1:
        prime_factors.append(number)
    return prime_factors
prime_factors = primeFactors()

print("Prime Factors Are:",prime_factors)