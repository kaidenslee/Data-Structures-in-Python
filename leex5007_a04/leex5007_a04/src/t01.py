"""

----------------------------------
Assignment 4, Task 1
----------------------------------
__updated__= "2024-02-01"
----------------------------------
"""

from Queue_circular import Queue

target = Queue(2)

values = ["apples", 'peaches', 'clovers']

print("original list of values: apples, peaches, clovers")
print("capacity set to 2")
for i in values:
    target.insert(i)

print("queue:")
for i in target:
    print(i)

target.remove()

print("queue after remove()")
for i in target:
    print(i)

print("is queue full?")
print(target.is_full())
