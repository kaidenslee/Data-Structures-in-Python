"""

----------------------------------
Lab 3, Task 2
----------------------------------
__updated__= "2024-01-23"
----------------------------------
"""
from Queue_array import Queue

from utilities import queue_to_array
from utilities import array_to_queue

queue = Queue()


source = ['apples', 'cookies', 'icecream', 'strawberries']

print(array_to_queue(queue, source))

print("queue: ")
for i in queue:
    print(i)

target = []

print(queue_to_array(queue, target))


print(f"target:  {target}")
