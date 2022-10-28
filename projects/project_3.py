def main():
    choice1 = input('Welcome to Treasure Island.\n\
        Your mission is to find the treasure.\n\
        You''re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
    if choice1 == "left":
        choice2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
        if choice2 == "wait":
            choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n').lower()
            
            match choice3:
                case "red":
                    print("It's a room full of fire. Game over.")
                case "blue":
                    print("You enter a room with beasts. Game over.")
                case "yellow":
                    print("You found the Treasure! You win!")
                case _:
                    print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You got attaced by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")