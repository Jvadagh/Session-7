"""
17. Write a function named print_big_enough that accepts two parameters, a list of numbers and a
number. The function should print, in order, all the elements in the list that are at least as large as the
second parameter.
THE ANSWER IS :
"""
lst = [1, 2, 3, 4, 5, 6]
num = 2


def print_big_enough(lst, num):
    sliced_lst = []
    for i in lst:
        if i >= num:
            sliced_lst += [i]

    print(sliced_lst)


print_big_enough(lst, num)
