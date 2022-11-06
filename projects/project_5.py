"""
    Using ASCII numbers:
        33 - 43 special characters
        48 - 57 numbers
        65 - 90, 97 - 122 uppercase, lowercase characters
"""
import random

def main():
    print("Welcome to the PyPassword Generator!")
    #assuming only numbers are being used as input
    num_letters = int(input("How many LETTERS would you like in your password? "))
    num_symbols = int(input("How many SYMBOLS would you like in your password? "))
    num_numbers = int(input("How many NUMBERS would you like in your password? "))

    password = ""

    #create password with letters, symbols and numbers in order and then shuffle them

    while num_letters > 0:
        #randomly choose upper or lowercase letters
        match (random.randint(1, 2)):
            #upper case
            case 1:
                password += chr(random.randint(65, 90))
            #lower case
            case 2:
                password += chr(random.randint(97, 122))
        num_letters -= 1

    while num_symbols > 0:
        password += chr(random.randint(33, 43))
        num_symbols -= 1

    while num_numbers > 0:
        password += chr(random.randint(48, 57))
        num_numbers -= 1

    #randomize password string by converting it to an array, shuffling it and the putting it back together.
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    print(password)