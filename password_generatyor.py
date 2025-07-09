import random

#all possible characters the password could be
possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_"

#prompt the user a message asking them how long they want their password to be (max of 16)
password_length = int(input("Enter desired password length (MAX 16): "))

# prints this message out if the user wants a password over 16 characters
if password_length > 16:
    print("Password length must be less than 16")
# elif statement if the user inputs 0 or a negative number
elif password_length <= 0:
    print("Please enter a number 1-16")
# generates the password if all conditions are satisfactory
else:
    password = ''.join(random.choice(possible_characters) for _ in range(password_length))
    print(password)
