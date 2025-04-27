"""

----------------------------------
Assignment 2, Task 4
----------------------------------
__updated__= "2024-01-14"
----------------------------------
"""
from Food_utilities import food_table

from Food import Food

food = Food("Curry Chicken", 2, False, 320)
food1 = Food("Apple", 0, True, 90)
food2 = Food("Pizza", 1, False, 120)
foods = [food, food1, food2]


print(food_table(foods))
