print('BASIR P. WAHAB')
print('1BSCE-B')
print()
print('ICT 09 Programming 1')
print('FINAL PROJECT')
print()
print('PYTHON PROJECT 8 - PASSWORD GENERATOR')
print()
print()

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits  
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    password_length = 8  
    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")
