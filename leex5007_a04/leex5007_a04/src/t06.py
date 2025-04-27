"""

----------------------------------
Assignment 4, Task 6
----------------------------------
__updated__= "2024-02-01"
----------------------------------
"""
from Priority_Queue_array import Priority_Queue


source = Priority_Queue()

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

key = 5

print("values = 1, 2, 3, 4, 5, 6, 7, 8")
print("key = 5")
for i in values:
    source.insert(i)

print(source.split_key(key))
