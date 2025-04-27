"""

----------------------------------
Assignment 5, Task 1
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-02-10"
----------------------------------
"""
from Sorted_List_array import Sorted_List

source = [1, 1, 2, 2]
sourceagain = []

source1 = Sorted_List()
source2 = Sorted_List()

for i in source:
    source1.insert(i)

for i in sourceagain:
    source2.insert(i)

key = 2

target = Sorted_List()


print(source1.clean())
