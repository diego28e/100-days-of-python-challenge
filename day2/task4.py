#BMI calculator
#Weight divided by height squared

weight=float(input("What's your weight?\n"))
height=float(input("What's your height?\n"))
BMI= weight/height ** 2

if BMI >= 40:
    print("You are Obese class III. "+ "Your BMI is equal to: " +str(round(BMI,2)))
elif BMI >= 35:
    print("You are Obese class II. " + "Your BMI is equal to: " + str(round(BMI,2)))
elif BMI >= 30:
    print("You are Obese class I. " + "Your BMI is equal to: " + str(round(BMI,2)))
elif BMI >= 25:
    print("You are overweight. " + "Your BMI is equal to: " + str(round(BMI,2)))
else:
    print(f"Your weight is normal. Your BMI is equal to: {round(BMI, 2)}" )

# Adding the 'f' to the beginning of the string will make sure that it converts types correctly as long as we put variables inside curly braces