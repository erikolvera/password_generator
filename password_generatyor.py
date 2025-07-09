import random

possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_"

password = ''.join(random.choice(possible_characters) for _ in range(16))

print(password)