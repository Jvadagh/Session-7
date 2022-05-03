"""9. An assignment statement containing the expression a[m:n] on the left side and a list on the right
side can modify list a. Complete the following table by supplying the m and n values in the slice
assignment statement needed to produce the indicated list from the given original list.

A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] ==> A[0:5] ==> [2, 4, 6, 8, 10]

A = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10] ==> A[6:11] ==> [2, 4, 6, 8, 10]

A = [2, 3, 4, 5, 6, 7, 8, 10] ==> A[0:7:2] + A[7:] ==>! [2, 4, 6, 8, 10]

A = [2, 4, 6, 'a', 'b', 'c', 8, 10] ==> A[0:3] + A[6:] ==> [2, 4, 6, 8, 10]

A = [2, 4, 6, 8, 10] ==> A[0:5] ==> [2, 4, 6, 8, 10]

A = [] ==> IMPOSSIBLE !! HOWEVER => A[0:] + [2, 4, 6, 8, 10] ==> [2, 4, 6, 8, 10]

A = [10, 8, 6, 4, 2] ==> A[-1:-6:-1] ==> [2, 4, 6, 8, 10]

A = [2, 4, 6] ==> IMPOSSIBLE !! HOWEVER => A[0:4] + [8, 10] ==> [2, 4, 6, 8, 10]

A = [6, 8, 10] ==> IMPOSSIBLE !! HOWEVER => [2, 4] + A[0:4] ==> [2, 4, 6, 8, 10]

A = [2, 10] ==> IMPOSSIBLE !! HOWEVER => A[0:1] + [4, 6, 8] + A[1:2] ==> [2, 4, 6, 8, 10]

A = [4, 6, 8] ==> IMPOSSIBLE !! HOWEVER => [2] + A[0:3] + [10] ==> [2, 4, 6, 8, 10]"""