import random
import my_module

random_integer=random.randint(1, 10)
random_result=(round(random_integer*my_module.favorite_number,2))
final_result=int(random_result*100)
print(final_result)
