print("Welcome to the rollercoaster")
height=int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster.")
    age=int(input("What's your age?"))
    if age<12:
        print("Your ticket costs $5 USD")
    elif age<=18:
        print("Your ticket costs $7 USD")
    else:
        print("Your ticket costs $12 USD")
else:
    print("Sorry, but you need to grow taller")