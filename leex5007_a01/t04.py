"""

----------------------------------
Assignment 1, Task 4
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-09"
----------------------------------
"""
from functions import file_analyze

fv = open("customers.txt", "r", encoding="utf-8")


print(file_analyze(fv))
fv.close
