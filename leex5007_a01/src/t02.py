"""

----------------------------------
Assignment 1, Task 2
----------------------------------
__updated__= "2024-01-08"
----------------------------------
"""
from functions import list_subtraction

minuend = []
subtrahend = []
length = int(input("Enter number of values in list: "))

for i in range(length):
    num = int(input("Enter number to add: "))
    minuend.append(num)

subtrahend.append(int(input("Enter number to search for: ")))

print(list_subtraction(minuend, subtrahend))
