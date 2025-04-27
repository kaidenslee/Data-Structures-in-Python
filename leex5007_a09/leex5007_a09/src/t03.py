"""

----------------------------------
Assignment 9, Task 1
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-03-23"
----------------------------------
"""
from functions import insert_words
from functions import comparison_total
from Hash_Set_BST import Hash_Set

fv = open('otoos610.txt', 'r', encoding="utf-8")
hash_set = Hash_Set(20)

insert_words(fv, hash_set)
total, max_word = comparison_total(hash_set)

print("Using array-based list Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(
    max_word.word, max_word.comparisons))
