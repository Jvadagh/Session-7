"""
21. Provide five different ways to create the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and assign it to
the variable lst.
"""


# 1
def first_way():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a)


# 2
def second_way():
    a = []

    for i in range(1, 11):
        a += [i]
    print(a)


# 3
def third_way():
    a = []
    i = 1
    while i < 11:
        a.append(i)
        i += 1
    print(a)


def fourth_way():
    b = [-10, -9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    a = (b[3:13])
    print(a)


def fifth_way(n, a):
    if 11 > n > 0:
        a += [n]
        fifth_way(n + 1, a)
    return a

#1
first_way()
#2
second_way()
#3
third_way()
#4
fourth_way()
#5
print(fifth_way(1, []))
