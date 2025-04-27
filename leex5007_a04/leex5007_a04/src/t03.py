"""

----------------------------------
Assignment 4, Task 3
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-31"
----------------------------------
"""

from Queue_array import Queue
from functions import queue_split_alt

source = Queue()

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("original queue: 1, 2, 3, 4, 5, 6, 6, 7, 8, 9")
for i in values:
    source.insert(i)

print(queue_split_alt(source))
