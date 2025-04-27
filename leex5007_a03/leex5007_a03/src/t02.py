"""

----------------------------------
Assignment 3, Task 2
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-20"
----------------------------------
"""

from Stack_array import Stack

values = [5, 8, 12, 8]
values2 = [3, 6, 1, 7, 9, 14]

source1 = Stack()
source2 = Stack()

while len(values) > 0:
    source1.push(values.pop())

while len(values2) > 0:
    source2.push(values2.pop())


target = Stack()

target.combine(source1, source2)

for i in target:
    print(i)
