''' 
@Author : Tushal Kumar
@Date : 2021-11-07
@Tittle : User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

'''
@Desc :  Take User Name as Input. Ensure UserName has min 3 char
'''


def replace(username): 
    if(len(username) < 3) :
        return "username should not less minimum 3 character:"
    else:
        return "Hello "+username+" How are you"
    
    
username = input("Enter username:")
new_message = replace(username)
print(new_message)