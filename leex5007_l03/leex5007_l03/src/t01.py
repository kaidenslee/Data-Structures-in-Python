"""

----------------------------------
Lab 3, Task 1
----------------------------------
__updated__= "2024-01-23"
----------------------------------
"""
from Queue_array import Queue

from utilities import array_to_queue

queue = Queue()

source = ['apples', 'cookies', 'icecream', 'strawberries']

print(f"source: {source}")

print(array_to_queue(queue, source))


print("queue:")
for i in queue:
    print(i)
