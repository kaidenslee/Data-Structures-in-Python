"""

----------------------------------
Assignment 5, Task 1
----------------------------------
__updated__= "2024-02-10"
----------------------------------
"""
from List_array import List
from Food import Food

source = [1, 2, 6, 8, 5, 4]
sourceagain = [1, 2, 6, 8, 5, 12, 12, 11, 10]

source1 = List()
source2 = List()

for i in source:
    source1.append(i)

for i in sourceagain:
    source2.append(i)

target = List()

key = 3

print(target.union(source1, source2))
