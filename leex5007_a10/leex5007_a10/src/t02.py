"""

----------------------------------
Assignment 10, Task 1
----------------------------------
__updated__= "2024-03-19"
----------------------------------
"""
from Sorts_List_linked import Sorts
from List_linked import List


list = [10223, 23, 3, 41, 522323]

llist = List()

for i in list:
    llist.append(i)


Sorts.radix_sort(llist)

for i in llist:
    print(i)
