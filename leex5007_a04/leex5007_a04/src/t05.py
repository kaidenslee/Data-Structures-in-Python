"""

----------------------------------
Assignment 4, Task 5
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-31"
----------------------------------
"""
from Priority_Queue_array import Priority_Queue

from functions import pq_split_key


source = Priority_Queue()

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = 5
print("values = 1, 2, 3, 4, 5, 6, 7, 8, 9")
print("key = 5")

for i in values:
    source.insert(i)

print(pq_split_key(source, key))
