"""

----------------------------------
Assignment 1, Task 7
----------------------------------
__updated__= "2024-01-09"
----------------------------------
"""
from functions import max_diff

a = []

length = int(input("Enter number of values in list: "))

for i in range(length):
    num = int(input("Enter number to add: "))
    a.append(num)

print(max_diff(a))
