"""

----------------------------------
Assignment 7, Task 1
----------------------------------
__updated__= "2024-03-04"
----------------------------------
"""
from Sorted_List_linked import Sorted_List

list = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]

llist = Sorted_List()
llist2 = Sorted_List()

for i in list:
    llist.insert(i)

for i in list2:
    llist2.insert(i)

print(llist.min())
