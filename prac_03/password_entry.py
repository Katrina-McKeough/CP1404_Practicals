"""
Katrina McKeough
"""


def main():
    min_password_length = 4
    password = get_password(min_password_length)
    print_asterisks(password)


def get_password(min_password_length):
    password = input("Please enter a password (minimum {} characters): ".format(min_password_length))
    while len(password) < min_password_length:
        print("Password too short!")
        password = input("Please enter a password (minimum {} characters): ".format(min_password_length))
    return password


def print_asterisks(password):
    print('*' * len(password))


main()
