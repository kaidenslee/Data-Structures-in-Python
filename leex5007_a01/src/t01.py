"""

----------------------------------
Assignment 1, Task 1
----------------------------------
__updated__= "2024-01-08"
----------------------------------
"""
from functions import clean_list
values = []

length = int(input("Enter number of values in list: "))

for i in range(length):
    num = int(input("Enter number to add: "))
    values.append(num)

print(f"{clean_list(values)}")
