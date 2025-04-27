"""

----------------------------------
Assignment 6, Task 1
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-02-13"
----------------------------------
"""
from Queue_linked import Queue

list = [1, 2, 3, 4, 5, 6]

queue = Queue()

for i in list:
    queue.insert(i)


target = Queue()

target._move_front_to_rear(queue)

for i in target:
    print(i)
