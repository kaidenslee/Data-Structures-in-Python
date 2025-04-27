"""

----------------------------------
Assignment 3, Task 7
----------------------------------
Author: Kaiden Lee
ID: 169050073
Email: leex5007@mylaurier.ca
__updated__= "2024-01-20"
----------------------------------
"""

from Stack_array import Stack
from functions import stack_maze

maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
        'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}

print(stack_maze(maze))
