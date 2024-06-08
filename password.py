import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    if not any(char.isdigit() for char in password):
        password = password[:random.randint(0, length - 1)] + random.choice(string.digits) + password[random.randint(0, length - 1):]

    return password

length = int(input("Enter the desired password length: "))

password = generate_password(length)

print(f"Your password is: {password}")
