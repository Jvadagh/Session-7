"""
18. Write a function named next_number that accepts a list of integer values. All the elements in the list
are unique, and all elements in the list are greater than or equal to one. (The caller must ensure that
these conditions are met before passing the list to next_number.) The next_number function should
return the smallest positive integer not in the list. (Note that 1 is the smallest positive integer.)
As examples,
• next_number([5, 3, 1]) would return 2
• next_number([5, 4, 1, 2]) would return 3
• next_number([2, 3]) would return 1
• next_number([]) would return 1
THE ANSWER IS :
"""
lst = [5, 3, 1]


def next_number(lst):
    mymax = 0
    num = 0
    for i in lst:
        if i > mymax:
            mymax = i

    for i in range(1, mymax + 1):
        if i not in lst:
            return i

    return mymax + 1


print(next_number(lst))


