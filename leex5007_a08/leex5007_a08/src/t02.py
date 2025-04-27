"""

----------------------------------
Assignment 8, Task 1
----------------------------------
__updated__= "2024-03-13"
----------------------------------
"""
from functions import comparison_total
from functions import do_comparisons
from functions import letter_table
from Letter import Letter
from BST_linked import BST

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


bst1 = BST()
bst2 = BST()
bst3 = BST()

for i in DATA1:
    var = Letter(i)
    bst1.insert(var)

for i in DATA2:
    var = Letter(i)
    bst2.insert(var)

for i in DATA3:
    var = Letter(i)
    bst3.insert(var)

fn = "miserables.txt"
fv = open(fn, "r", encoding="utf-8")
do_comparisons(fv, bst1)
t1 = comparison_total(bst1)
fv = open(fn, "r", encoding="utf-8")
do_comparisons(fv, bst2)
t2 = comparison_total(bst2)
fv = open(fn, "r", encoding="utf-8")
do_comparisons(fv, bst3)
t3 = comparison_total(bst3)
print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("{}".format(t1))
print("------------------------------------------------------------")
print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
print("{}".format(t2))
print("------------------------------------------------------------")
print("Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ")
print("{}".format(t3))
print("------------------------------------------------------------")
letter_table(bst1)
