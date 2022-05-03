"""11. Write the list represented by each of the following list comprehension expressions."""
# (a) [x + 1 for x in [2, 4, 6, 8]] ==>
a = [3, 5, 7, 9]
# (b) [10*x for x in range(5, 10)] ==>
b = [50, 60, 70, 80, 90]
# (c) [x for x in range(10, 21) if x % 3 == 0] ==>
c = [12, 15, 18]
# (d) [(x, y) for x in range(3) for y in range(4)] ==>
d = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
# (e) [(x, y) for x in range(3) for y in range(4) if (x + y) % 2 == 0] ==>
e = [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]
