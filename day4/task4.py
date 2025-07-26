#Heads or tails
import random

initial_seed = int(random.uniform(0,9))
print(initial_seed)

if initial_seed % 2 == 0:
    print("Heads")
else:
    print("Tails")