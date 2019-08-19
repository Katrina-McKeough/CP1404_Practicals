"""
Katrina McKeough
"""

min_password_length = 4
password = input("Please enter a password (minimum {} characters): ".format(min_password_length))

while len(password) < min_password_length:
    print("Password too short!")
    password = input("Please enter a password (minimum {} characters): ".format(min_password_length))
print('*' * len(password))
