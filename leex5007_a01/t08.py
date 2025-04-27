"""

----------------------------------
Assignment 1, Task 8
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-09"
----------------------------------
"""
import random
from functions import matrix_stats


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
low = float(input("Enter low value of range: "))
high = float(input("Enter high value of range: "))
value_type = str(input("Enter value type (float/int): "))

a = []
count = 0

if value_type == "float":
    for i in range(rows):
        a.append([])
        for j in range(cols):
            a[count].append(random.uniform(low, high))
        count += 1
elif value_type == "int":
    for i in range(rows):
        a.append([])
        for j in range(cols):
            a[count].append(random.randint(low, high))
        count += 1

print(a)
print(matrix_stats(a))
