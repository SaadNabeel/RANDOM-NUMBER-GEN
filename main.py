import random
import string

def generatepassword(length=12):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    
    
    allcharacters = lowercase + uppercase + numbers
    

    password = ''.join(random.choice(allcharacters) for _ in range(length))
    
 
    passwordlist = list(password)
    random.shuffle(passwordlist)
    password = ''.join(passwordlist)
    
    return password


print("Generated Password:", generatepassword(12))
