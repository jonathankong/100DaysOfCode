def tip_calculator():
    print('Welcome to the tip calculator.')
    total = float(input('What was the total bill? $'))
    tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
    num_of_people = int(input('How many people to split the bill? '))
    split_payment = round(total * (1 + tip / 100) / num_of_people, 2)
    print(f'Each person should pay: ${split_payment}')

    