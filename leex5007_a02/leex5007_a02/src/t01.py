"""

----------------------------------
Assignment 2, Task 1
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-14"
----------------------------------
"""
from Food_utilities import by_origin

from Food import Food

food = Food("Curry Chicken", 2, False, 320)
food1 = Food("Apple", 0, True, 90)
food2 = Food("Pizza", 1, False, 120)
foods = [food, food1, food2]

origin = int(input("Enter origin: "))


v = by_origin(foods, origin)

for s in v:
    print(s)
