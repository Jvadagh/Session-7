"""
16. Complete the following function that counts the even numbers in a list of integers. For example, if
list a contains the elements 3;5;4;􀀀1; and 0, the call count_evens(a) would evaluate to 2, since a
contains two even numbers: 4 and 0. The function returns zero if the list is empty. The function does
not affect the contents of the list.
THE ANSWER IS :
"""
lst = [3,5,4,-1,0]

def count_evens(lst):
    evens_num = 0
    for i in lst:
        if i % 2 == 0:
            evens_num = evens_num + 1
    print(evens_num)

count_evens(lst)