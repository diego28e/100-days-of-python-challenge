#logical operators
#and
#or
#not

#Example with the midlife crisis offer
print("Welcome to the rollercoaster")
height=int(input("What's your height in cm?"))
bill = 0

if height >=120:
    print("You can ride the rollercoaster")
    age=int(input("What's your age?"))
    if age <= 12:
        bill=5
        print("Child tickets are $5")
    elif age <=18:
        bill=7
        print("Youth tickets are $7")
    elif 45 <= age <= 55:
        print("You'll get a free ride")
    else:
        bill=12
        print("Adult tickets are $12")
    want_photo = input("Do you want to have a photo take? Type y for Yes or n for No.\n")
    if want_photo == "y":
        bill +=3
    print(f"The cost of your ticket is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")