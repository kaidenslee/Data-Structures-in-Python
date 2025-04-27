"""

----------------------------------
Assignment 10, Task 1
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-03-19"
----------------------------------
"""
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque


list = [10223, 23, 3, 41, 522323]

llist = Deque()

for i in list:
    llist.insert_rear(i)


Sorts.gnome_sort(llist)

for i in llist:
    print(i)
