"""

----------------------------------
Lab 3, Task 4
----------------------------------
__updated__= "2024-01-23"
----------------------------------
"""
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq

source = [22, 33, 11, 55, 44]
print(f"source: {source}")
pq = Priority_Queue()

print(array_to_pq(pq, source))

print("priority queue: ")
for i in pq:
    print(i)
