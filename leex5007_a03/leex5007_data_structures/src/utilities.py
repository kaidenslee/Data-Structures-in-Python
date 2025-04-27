"""
-------------------------------------------------------
Utilities Functions
-------------------------------------------------------
This file was originally provided as a template. Not my 
personal work.
__updated__ = "2024-01-16"
-------------------------------------------------------
"""
from Food import Food
from Stack_array import Stack

# task 1


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while len(source) > 0:
        stack.push(source.pop(len(source)-1))

    return

# task 2


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while stack.is_empty() == False:
        target.insert(0, stack.pop())

    return

# task 3


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    stack = Stack()

    print(f"is_empty expects True: {stack.is_empty()}")
    n = source.pop()
    stack.push(n)
    print(f"{n} was pushed onto stack.")
    print(f"is_empty expects False: {stack.is_empty()}")
    print(f"peek expects {n}: {stack.peek()}")
    m = stack.pop()
    print(f"{m} was popped off of stack.")
    print(f"is_empty expects True: {stack.is_empty()}")

    return None
