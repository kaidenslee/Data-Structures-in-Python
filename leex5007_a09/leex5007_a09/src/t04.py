"""

----------------------------------
Assignment 9, Task 4
----------------------------------
__updated__= "2024-03-18"
----------------------------------
"""
from BST_linked import BST

list = [1, 2, 3, 4, 5]

bst = BST()

for i in list:
    bst.insert(i)

print(bst.parent_r(4))
