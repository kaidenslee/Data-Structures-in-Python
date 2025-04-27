"""

----------------------------------
Assignment 3, Task 1
----------------------------------
__updated__= "2024-01-20"
----------------------------------
"""
from functions import stack_combine
from Stack_array import Stack

values = [5, 8, 12, 8]
values2 = [3, 6, 1, 7, 9, 14]

source1 = Stack()
source2 = Stack()

while len(values) > 0:
    source1.push(values.pop())

while len(values2) > 0:
    source2.push(values2.pop())


target = stack_combine(source1, source2)

for i in target:
    print(i)
