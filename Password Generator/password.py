import random
password = ""
for i in range(32):
    password += chr(random.randint(32, 126))

print(password)
