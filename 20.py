"""
20. Write a Python program that creates the matrix
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
and assigns it to the variable m. Pretty print m to ensure the contents are correct. Next, reassign
m[2][4] to 0, and print m again to ensure your code modified the correct element.
"""

def matrix(satr,sotoon):
    result = []
    for i in range(satr):
        partial_result = []
        for i in range(sotoon):
            partial_result.append(1)
        result.append(partial_result)

    return result

m = matrix(6, 9)
for i in m:
    print(i)

m[2][4] = 0
print("---------------------------")
for i in m:
    print(i)