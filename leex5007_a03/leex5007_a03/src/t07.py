"""

----------------------------------
Assignment 3, Task 7
----------------------------------
__updated__= "2024-01-20"
----------------------------------
"""

from Stack_array import Stack
from functions import stack_maze

maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
        'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}

print(stack_maze(maze))
