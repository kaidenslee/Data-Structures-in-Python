"""

----------------------------------
Assignment 4, Task 4
----------------------------------
__updated__= "2024-01-31"
----------------------------------
"""

from Queue_array import Queue


source = Queue()

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("original queue: 1, 2, 3, 4, 5, 6, 7, 8, 9")
for i in values:
    source.insert(i)

target1, target2 = source.split_alt()
