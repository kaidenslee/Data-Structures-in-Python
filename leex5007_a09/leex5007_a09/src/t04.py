"""

----------------------------------
Assignment 9, Task 4
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-03-18"
----------------------------------
"""
from BST_linked import BST

list = [1, 2, 3, 4, 5]

bst = BST()

for i in list:
    bst.insert(i)

print(bst.parent_r(4))
