from modules.project_8_art import LOGO
import math
#using ASCII: 65 - 90 uppercase, 97 - 122 lowercase
def main():
    print(LOGO + '\n')
    coding = input('Type \'encode\' to encrypt, type \'decode\' to decrypt: ')
    message = input('Type your message: ')
    shift_value = int(input('Type your shift number: '))
    char_list = list(message)

    match(coding):
        case 'encode':
            for i in range(len(char_list)):
                char_value = ord(char_list[i])
                if char_value >= 65 and char_value <= 122:
                    new_char_value = char_value + shift_value
                    if new_char_value > 122:
                        new_char_value = 65 - 1 + (new_char_value % 122)
                    if new_char_value > 90 and new_char_value < 97:
                        new_char_value = new_char_value + 6
                    char_list[i] = chr(new_char_value)
        case 'decode':
            for i in range(len(char_list)):
                char_value = ord(char_list[i])
                if char_value >= 65 and char_value <= 122:
                    new_char_value = char_value - shift_value
                    if new_char_value < 65:
                        new_char_value = 122 - 1 - (abs(new_char_value) % 26)
                    if new_char_value > 90 and new_char_value < 97:
                        new_char_value = new_char_value - 6
                    char_list[i] = chr(new_char_value)
    print(''.join(char_list))
    
main()