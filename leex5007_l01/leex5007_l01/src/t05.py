"""

----------------------------------
Lab 1, Task 5
----------------------------------
__updated__= "2024-01-11"
----------------------------------
"""
from Food_utilities import read_foods
from Food import Food
file_variable = open('foods.txt', 'r', encoding="utf-8")

print(read_foods(file_variable))


file_variable.close()
