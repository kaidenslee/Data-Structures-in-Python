"""

----------------------------------
Assignment 3, Task 3
----------------------------------
__updated__= "2024-01-20"
----------------------------------
"""

from Stack_array import Stack
from functions import stack_reverse

values = [5, 8, 12, 8]

source = Stack()


while len(values) > 0:
    source.push(values.pop())

print("initial stack:")
for i in source:
    print(i)

print(stack_reverse(source))

print("reversed stack:")
for i in source:
    print(i)
