print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`-._` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
# def play_game():
#     print("Welcome to Treasure Island. \n Your mission is to find the treasure.")
#
#     decision1 = input("left or right?\n")
#     if decision1 != "left":
#         print("You've fallen into a hole. Gave Over.")
#         return
#     decision2 = input("Swim or wait\n")
#     if decision2 != "wait":
#         print("You've been attacked by a trout. Gave Over")
#         return
#     decision3 = input("Which door do you wanna go through? red, blue or yellow??\n")
#     if decision3 != "yellow":
#         if decision3 == "red":
#             print("Burned by fire. Gave Over")
#         elif decision3 == "blue":
#             print("Eaten by beasts. Gave Over")
#         else:
#             print("Gave over")
#         return
#     else:
#         print("You win!!")
#
# play_game()

print("Welcome to Treasure Island. \n Your mission is to find the treasure.")

decision1 = input("left or right?\n").lower()
if decision1 == "left":
    decision2 = input("Swim or wait\n").lower()
    if decision2 == "wait":
        decision3 = input("Which door do you wanna go through? red, blue or yellow??\n").lower()
        if decision3 == "yellow":
            print("You win!!")
        elif decision3 == "red":
            print("Burned by fire. Game Over")
        elif decision3 == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game over")
    else:
        print("You've been attacked by a trout. Game Over")
else:
    print("You've fallen into a hole. Game Over.")