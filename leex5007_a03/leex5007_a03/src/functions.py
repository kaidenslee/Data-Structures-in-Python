"""

----------------------------------
Functions, Assignment 3
----------------------------------
__updated__= "2024-01-20"
----------------------------------
"""
from Stack_array import Stack

# Constants
OPERATORS = "+-*/"

# task 1


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()

    while not (source1.is_empty() and source2.is_empty()):
        if source1.is_empty():
            target.push(source2.pop())
        elif source2.is_empty():
            target.push(source1.pop())
        else:
            target.push(source1.pop())
            target.push(source2.pop())

    return target


# task 3


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    hold = []
    while source.is_empty() == False:
        hold.insert(0, source.pop())

    while len(hold) > 0:
        source.push(hold.pop())

    return None


# task 5

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = False
    chars = ""
    check_string = ""

    for s in string:
        if s.isalpha():
            chars += s.lower()

    check = Stack()
    for i in range(len(chars)):
        check.push(chars[i])

    while check.is_empty() == False:
        check_string += (check.pop())

    if check_string == chars:
        palindrome = True

    return(palindrome)


# task 6

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    values = Stack()

    string = string.split()

    for i in string:
        if i not in OPERATORS:
            values.push(i)
        if i in OPERATORS:
            top = float(values.pop())
            bottom = float(values.pop())
            if i == "+":
                values.push(bottom + top)
            elif i == "-":
                values.push(bottom - top)
            elif i == "*":
                values.push(bottom*top)
            elif i == "/":
                values.push(bottom/top)

    answer = values.pop()

    return answer


# task 7

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()
    path = []
    current = "Start"

    while current != "X":
        path.append(current)
        choices = maze[current]

        if not choices:
            if stack.is_empty():
                return None
            current = stack.pop()
        else:
            next_point = choices.pop()
            stack.push(current)
            current = next_point

    path.append("X")
    return path
