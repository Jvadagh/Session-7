"""
15. Complete the following function that adds up all the positive values in a list of integers. For example,
if list a contains the elements 3;􀀀3;5;2;􀀀1; and 2, the call sum_positive(a) would evaluate to 12,
since 3+5+2+2 = 12. The function returns zero if the list is empty.
THE ANSWER IS :
"""
a = [3, -3, 5, 2, -1, 2]


def sum_positive(a):
    sum = 0
    for i in a:
        if i > -1:
            sum = sum + i
    print(sum)

sum_positive(a)