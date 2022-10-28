import random

#region CONST
PLAYER_OPTIONS = [
""" 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""  
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
,"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

COMPUTER_OPTIONS = [
"""
   _______    
  (____   '---
 (_____)      
 (_____)      
  (____)      
   (___)__.---
"""
,"""  
      _______     
 ____(____    '---
(______           
(_______          
 (_______         
  (__________.---
"""
,"""   
       _______    
  ____(____   '---
 (______          
(__________       
      (____)      
       (___)__.---
"""]

OPTION_NAMES = ['Rock', 'Paper', 'Scissors']
#endregion

def main():

    print("Welcome to Rock Paper Scissors!\n")
    while True:
        try:
            choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            if choice > 2 or choice < 0:
                print ("Try Again\n")
            else:
                break
        except:
            print("Try Again\n")

    comp_choice = random.randint(0, 2)

    result = ''

    if choice == comp_choice:
        result = "Draw"
    elif (choice == 0 and comp_choice == 1) or (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 0):
        result = "You lose"
    else:
        result = "You win"

    print(f'You chose {OPTION_NAMES[choice]}                {PLAYER_OPTIONS[choice]} ')
    print(f'The computer chose {OPTION_NAMES[comp_choice]}  {COMPUTER_OPTIONS[comp_choice]}')
    print(result)