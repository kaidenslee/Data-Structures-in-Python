"""

----------------------------------
Assignment 2, Task 4
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-14"
----------------------------------
"""
from Food_utilities import food_search

from Food import Food

food = Food("Curry Chicken", 2, False, 320)
food1 = Food("Apple", 0, True, 90)
food2 = Food("Pizza", 1, False, 120)
foods = [food, food1, food2]

origin = int(input("Enter food origin:"))
max_cals = int(input("Enter max number of calories: "))
is_veg = True
print("is_veg = True")

v = food_search(foods, origin, max_cals, is_veg)

for s in v:
    print(s)
