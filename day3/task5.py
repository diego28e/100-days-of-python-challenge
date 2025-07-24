print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0

# if size=="S" or size=="s":
#     bill=15
#     if pepperoni=="y":
#         bill+=2
# elif size =="M" or size=="m":
#     bill=20
#     if pepperoni=="y":
#         bill+=3
# else:
#     bill=25
#     if pepperoni=="y":
#         bill+=3
# if extra_cheese=="y":
#         bill+=1
#
# print(f"Your total bill is ${bill}")

if size == "s":
    bill += 15
elif size =="m":
    bill+= 20
elif size == "l":
    bill += 25
else:
    print("You typed the wrong inputs")

#todo: work out how much to add to the bill based on their pepperoni choice
if pepperoni == "y":
    if size == "s":
        bill+= 2
    else:
        bill +=3
#todo: work out the final amount based on whether they want extra cheese
if extra_cheese == "y":
    bill+=1

print(f"Your final bill is ${bill}")