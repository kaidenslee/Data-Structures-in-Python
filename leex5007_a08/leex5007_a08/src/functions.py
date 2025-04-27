"""

----------------------------------
Functions, Assignment 8
----------------------------------
__updated__= "2024-03-13"
----------------------------------
"""
from Letter import Letter


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    file_variable.seek(0)

    for line in file_variable:
        for char in line.strip():
            if char.isalpha():
                let = Letter(char.upper())
                bst.retrieve(let)

    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    letters = bst.inorder()
    for x in letters:
        total += x.comparisons

    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total = 0
    letters = bst.inorder()
    for x in letters:
        total += x.count

    print(f'''Letter Count/Percent Table
   
Total Count: {total:,})

Letter Count        %
---------------------''')
    for x in letters:
        print(f'{x.letter:>5}  {x.count:6,}  {x.count/total*100:>5.2f}%')

    return
