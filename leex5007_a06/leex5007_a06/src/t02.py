"""

----------------------------------
Assignment 6, Task 2
----------------------------------
__updated__= "2024-02-17"
----------------------------------
"""
from Priority_Queue_linked import Priority_Queue


list = [1, 2, 3, 4, 5, 6]

queue = Priority_Queue()

for i in list:
    queue.insert(i)


target = Priority_Queue()

target._move_front_to_rear(queue)

for i in target:
    print(i)
