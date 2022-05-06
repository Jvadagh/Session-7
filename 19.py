"""
Write a function named reverse that reorders the contents of a list so they are reversed from their
original order. a is a list. Note that your function must physically rearrange the elements within the
list, not just print the elements in reverse order.
"""
mylist = ['javad', 'aghajanloo', 1998, 2022]


def reverse(mylist):
    mylist2 = []
    for item in mylist:
        mylist2.insert(0, item)
    return mylist2


print(reverse(mylist))
