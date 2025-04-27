"""

----------------------------------
Lab 2, Task 3
----------------------------------
__updated__= "2024-01-16"
----------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack
from utilities import stack_to_array


stack = Stack()

source = ['apples', 'bananas', 'eggs', 'beans']
print(array_to_stack(stack, source))

print("stack: ")
for i in stack:
    print(i)

target = []
print(stack_to_array(stack, target))

print(f"target = {target}")
