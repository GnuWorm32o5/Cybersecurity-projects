import random
import string

num = int(input("Enter a number to generate a password of the same lenght size: "))

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation

pool = upper + lower + digits + punctuation

characters = []
for i in range(num):
    characters.append(random.choice(pool))

random.shuffle(characters)
password = "".join(characters)
print(f"Your password is: {password}")
