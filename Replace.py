def replace(username): 
    if(len(username) < 3) :
        return "username should not less minimum 3 character:"
    else:
        return "Hello "+username+" How are you"
    
    
username = input("Enter username:")
new_message = replace(username)
print(new_message)