import random
import string

length = int(input("Enter the password length: "))
characters = string.ascii_letters + string.digits + string.punctuation # Creates a list of all characters
password = ""
for i in range(length):
    password = password + random.choice(characters) # Randomly selects characters to create a password
print("New password:", password)