favorite_number = 2736

import random

# def generate_random_num():
#     random_num = random.randint(0,favorite_number)
#     return random_num

def difference_of_numbers(number):
   difference = number - random.randint(0, favorite_number)
   return difference


def run_difference():
   differnce = difference_of_numbers(favorite_number)
   print(differnce)

run_difference()
# favorite_number = 2736     
def is_equal():
    num = -1
    count = 0
    while num != favorite_number:
        num = random.randint(0, favorite_number*2)
        count += 1
    print(f"It took the computer {count} attempts to guess my favorite number.")
        
is_equal()
