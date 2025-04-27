"""

----------------------------------
Lab 4, Task 2
----------------------------------
__updated__= "2024-01-30"
----------------------------------
"""
from utilities import list_to_array
from List_array import List

llist = List()

source = [11, 22, 33, 55]
print("source = [11, 22, 33, 55]")

for i in source:
    llist.append(i)

target = []


print(list_to_array(llist, target))
