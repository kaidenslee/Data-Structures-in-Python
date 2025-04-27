"""

----------------------------------
Lab 1, Task 7
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-11"
----------------------------------
"""
from Food_utilities import get_vegetarian
from Food_utilities import read_foods
from Food import Food
file_variable = open('foods.txt', 'r', encoding="utf-8")

foods = (read_foods(file_variable))

file_variable.close()

print(get_vegetarian(foods))
