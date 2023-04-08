import string
from random import choice

def get_user_length():
    """Get password length from user."""
    while True:
        try:
            nr_letters = int(input("Password length [number]: "))
            if nr_letters <= 2:
                print("Password length must be a positive integer.Minim 3 characters long! ")
            else:
                return nr_letters
        except ValueError:
            print("Please enter a valid integer for the password length.")


def get_user_use_digits():
    """Get user's choice for using digits in password."""
    while True:
        digits = input("The password must have digits?[Y/N]:")
        if digits.upper() == "Y":
            return True
        elif digits.upper() == "N":
            return False   
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


def get_user_use_symbols():
    """Get user's choice for using symbols in password."""
    while True:
        symbols = input("Do you want to use symbols?[Y/N]: ")
        if symbols.upper() == "Y":
            return True
        elif symbols.upper() == "N":
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


password_length = get_user_length()
use_digits = get_user_use_digits()
use_symbols = get_user_use_symbols()


def same_character(param):
    j = 0
    for i in range(0,len(param)-1):
        if param[i] == param[i+1]:
            j += 1
    return j


while True:
    
    if use_digits and use_symbols:
        password = ''.join([choice(string.ascii_letters) for i in range(password_length-2)]) + choice(
            string.digits) + choice(string.punctuation)
    elif use_digits:
        password = ''.join([choice(string.ascii_letters) for i in range(password_length-1)]) + choice(
            string.digits)
    elif use_symbols:
        password = ''.join([choice(string.ascii_letters) for i in range(password_length-1)]) + choice(
            string.punctuation)
    else:
        password = ''.join([choice(string.ascii_letters) for i in range(password_length)])

    consecutivity = same_character(password)
    if consecutivity == 0:
        break
    else:
        continue

print(f'Your password is: {password}')
