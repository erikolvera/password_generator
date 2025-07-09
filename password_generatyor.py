import random

#all possible characters the password could be
possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_"

#prompt the user a message asking them how long they want their password to be
password_length = input("What password length would you like? MAX OF 16 CHARACTERS")


password = ''.join(random.choice(possible_characters) for _ in range(16))

print(password)