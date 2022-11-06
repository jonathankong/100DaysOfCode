from modules.project_10_art import LOGO

def main():
    print(LOGO)
    first_num = float(input('What\'s the first number?: '))
    answer = 0.0
    while True:
        operation = input('+\n-\n*\n/\nPick an operation: ')
        second_num = float(input('What\'s the next number?: '))
        answer = 0.0

        match operation:
            case '+':
                answer = first_num + second_num
            case '-':
                answer = first_num - second_num
            case '*':
                answer = first_num * second_num
            case '/':
                answer = first_num / second_num

        if (input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y"):
            first_num = answer
        else:
            break
        
    main()

main()