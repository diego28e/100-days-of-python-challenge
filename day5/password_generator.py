import random
# ✅ Lowercase letters only
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=', '+','{','}','|','.','<','>','?','/']

print("Welcome to the Password Generator!")
num_letters=int(input("How many letters would you like in your password?\n"))
num_numbers=int(input("How many numbers would you like?\n"))
num_symbols=int(input("How many symbols would you like?\n"))

user_password=[]
for i in range(1,num_letters+1):
    user_password.append(random.choice(letters))


for i in range(1,num_numbers+1):
    user_password.append(random.choice(numbers))
    random.shuffle(user_password)

for i in range(1,num_symbols+1):
    user_password.append(random.choice(symbols))
    random.shuffle(user_password)

random.shuffle(user_password)
final_password="".join(user_password)
print(f"Your super secure password is: {final_password}")