"""

----------------------------------
Assignment 4, Task 2
----------------------------------
__updated__= "2024-01-31"
----------------------------------
"""

from Queue_array import Queue

target = Queue()
source = Queue()

values = ["apples", "peaches"]
print("first queue: apples, peaches")
for i in values:
    target.insert(i)
print("second queue, apples")
values2 = ["apples"]

for i in values2:
    source.insert(i)

print(source == target)
