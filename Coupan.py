'''
@Auther : Tushal kumar
@Date : 2021-11-11
@Desc : Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
'''

import random



class Coupan():

    
    try:
            def generate(amount):

                
                coupon = open("coupons.txt", "a")  

                for x in range(0, amount):

                    a = random.randint(1000, 9999)
                    a = str(a)
                   

                    total = ""
                    total = str(total)
                    total = a 

                    
                    coupon.write(total)
                    coupon.write("\n")

                    
            if __name__ == "__main__" :
                amount = int(input("How many coupons do you want to generate: "))

                generate(amount)
            print("\nCode's have been generated!")    

    except ValueError:            
            print("\n please enter digit amount only")
        
            
