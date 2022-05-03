"""12. Provide a list comprehension expression for each of the following lists."""
# (a) [1, 4, 9, 16, 25] ==>
a = [x ** 2 for x in range(1, 6)]
# (b) [0.25, 0.5, 0.75, 1.0, 1.25. 1.5] ==>
b = [x + 0.25 for x in (0, 0.25, 0.50, 0.75, 1.00, 1.25)]
# (c) [('a', 0), ('a', 1), ('a', 2), ('b', 0), ('b', 1), ('b', 2)] ==>
c = [(x, y) for x in ('a', 'b') for y in range(0, 3)]
