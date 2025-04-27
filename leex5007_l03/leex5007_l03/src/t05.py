"""

----------------------------------
Lab 3, Task 5
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-24"
----------------------------------
"""
from Priority_Queue_array import Priority_Queue
from utilities import pq_to_array
from utilities import array_to_pq

source = ["strawberries", "marcus",
          "nicholson", "happy", "together"]

pq = Priority_Queue()

print(array_to_pq(pq, source))


target = []

print(pq_to_array(pq, target))
