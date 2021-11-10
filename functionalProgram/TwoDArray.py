'''
@Author : Tushal kumar
@Date : 2021-11-09
@Tittle : create 2 dimensional array in memory to read in M rows and N cols
'''

'''
@Desc :  A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
'''

row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)