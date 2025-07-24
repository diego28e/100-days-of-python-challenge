#Tip calculator

print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?\n$"))
tip=int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people=int(input("How many people to split the bill?\n"))
bill_with_tip = tip / 100 * bill + bill
result=bill_with_tip / people
print(f"Each person should pay: {round(result,2)}")