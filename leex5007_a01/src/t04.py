"""

----------------------------------
Assignment 1, Task 4
----------------------------------
__updated__= "2024-01-09"
----------------------------------
"""
from functions import file_analyze

fv = open("customers.txt", "r", encoding="utf-8")


print(file_analyze(fv))
fv.close
