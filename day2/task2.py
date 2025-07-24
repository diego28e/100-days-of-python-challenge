#Checking data types
print(type(True))
print(type("Hello"))
print(type(12345))
print(type(34.54))

#Type casting or type conversion
#convert int into string to get its length
print(len(str(1234445)))

print(type(int("123")))


#We can convert into
#int()
#float()
#str()
#bool()

#Challenge, fix the following statement
#print("Number of letters in your name: " + len(input("Enter your name:\n")))
print("Number of letters in your name: " + str(len(input("Enter your name:\n"))))