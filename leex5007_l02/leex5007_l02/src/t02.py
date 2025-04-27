"""

----------------------------------
Lab 2, Task 2
----------------------------------
__updated__= "2024-01-16"
----------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack


stack = Stack()

source = ['apples', 'bananas', 'eggs', 'beans']
print(f"source = {source}")

print(array_to_stack(stack, source))

print("stack:")
for i in stack:
    print(f"{i}")
