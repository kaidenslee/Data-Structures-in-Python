"""

----------------------------------
Lab 2, Task 3
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-16"
----------------------------------
"""
from Stack_array import Stack
from utilities import stack_test

fh = open('foods.txt', 'r', encoding="utf-8")
source = []

for i in fh:
    source.append(i.strip())

print(stack_test(source))
