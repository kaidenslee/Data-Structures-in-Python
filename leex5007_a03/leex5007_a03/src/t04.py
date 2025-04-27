"""

----------------------------------
Assignment 3, Task 7
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-20"
----------------------------------
"""

from Stack_array import Stack


stack = Stack()

list = ['apples', 'bananas', 'peas', 'oranges']


while len(list) > 0:
    stack.push(list.pop())

print("initial stack: ")
for i in stack:
    print(i)


stack.reverse()

print("\nreversed stack: ")
for i in stack:
    print(i)
