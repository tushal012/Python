''' 
@Author : Tushal kumar
@Date : 2021-11-09
@Tittle :   Sum of three Integer adds to ZERO 
'''

'''
@Desc :  A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
'''

import math


try:
    def triplet (arr,arr_len,sum):
        for i in range(0,arr_len-2):
            for j in range(i+1,arr_len-1):
                for k in range(j+1,arr_len):
                    if(arr[i]+arr[j]+arr[k]==sum):
                        print(arr[i],arr[j],arr[k])

    arr=list(map(int,input().split()))
    arr_len=len(arr)
    sum=0
    triplet(arr,arr_len,sum)

except:
      print("No integer found whose sum is Zero")                      