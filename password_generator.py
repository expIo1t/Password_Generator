import random
import string

def generate_strong_password(lenght=30):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for i in range(lenght))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
                and any(c in string.punctuation for c in password)):
            return password
    
# Generate a password 30 characters long:   
password = generate_strong_password(30)
print("Password: ", password)