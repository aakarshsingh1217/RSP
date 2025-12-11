"""
say you have an arr like this: [0, 0, 0, ...., 0, 1, 1, 1, ...]
could be extremely large or conceptually infinite
need to find where val becomes 1
normal BS needs low, high (bounds of arr)
doesn't have this due to infinite array
you can instead expand search window expontentially
A[1], A[2], A[4], A[8], ...
stop when you find first 1
guarantees you pass transition point
If the transition is at index p:
You will check indices: 1, 2, 4, 8, …, until you reach or pass p.
At most log₂(p) probes.
now we know transition lies between: 
( previous power of 2 , current power of 2 ]
if first 1 is at index 13
test A[1], test A[2], test A[4], ..., test A[16] = 1
so transition lies between (8, 16]
now do binary search inside that range, which is size
8, takes another log base 2(8) = 3 comparisons
"""

"""
example: find sqrt(n) using only comparisons and multip
e.g. find sqrt(10)
we know 3^2 = 9 (too small), 4^2 = 16 (too big)
so sqrt(10) is around 3.162
can discover this using binary search
for n >= 1, the square root must lie between 1 and n
repeatedly compute midpoint m = (l + r) / 2
so m = (1 + 10) / 2 = 5.5
compare m^2 with n
if m^2 < n, square root must be larger, move l to m
if m^2 > n, square root must be smaller, move r to m
m^2 = 30.25 > 10, m is too large, now r should be 5.5
keep moving l and r to midpoints until they're equal
(e.g. when m^2 equals around n)
after log base 2 n steps, interval is small and approx
is good
"""

"""
a recurrence relation is an equation where a func
is defined in terms of itself, usually a smaller
input size
this is why recurrence relations naturally model
recursive algs - both describe something by reducing
problem into smaller versions of itself
recurrence relations work for divide and conquer algs
like mergesort, quicksort etc.
to analyze their running time, need a math way to
express "time for input size n equals time for smaller
input + some extra work" (that's a recurrence).
e.g. fibonacci sqeuence Fn = Fn-1 + Fn-2
is defined by func:
"""

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

"""
merge sort: T(n)=2T(n/2)+n
split into two halves -> two recursive calls
each half is size n/2
merge step costs n
"""

"""
For a divide and conquer recurrence:
    T(n) = a T(N/b) + f(n)
    - a = num subproblems
    - b = shrinkage factor
    - f(n) = cost of splitting/merging at each level

    to solve it, compare f(n) with n^(log base b (a))

    this quantity is amount of total work contrib. by leaves
    of recursion tree.

    three situations:

    case 1:
    
    f(n) = O(n^(log base b (a - epsilon)))
    - internal work per level grows slowly
    - leaves dominate
    T(n) = O(N^log base b(a))

    case 2:
    
    f(n) = Theta(n^(log base b (a)))
    - each level contributes the same
    - multiply contribution per level * num of levels
    T(n) = O(N^log base b(a) * log n)

    case 3:
    
    f(n) = Omega(n^log base b(a + epsilon)) & regularity
    holds
    - work at root dominates
    T(n) = theta(f(n))
"""

"""
There's basically rules for the master theorem 
that give the answers but you don't need to know that exactly
Think of it like this
for sorting
T(n) = 2 * T(n/2) + O(n)
so, each recursion, we make 2 more problems of half 
the size of the current problem and do O(n) work
so, if we make 2 problems of half the size its 
like doing the current problem again
and as we do O(n) work each time, basically, 
the work we do is: n * the number of times we can half the problem
we can half the problem log n times 
so solution is O(n log n)
Does that make sense?
"""

"""
Every time you recurse, problem size cuts in half:
n
n / 2
n / 4
n / 8
...
We stop when the size becomes 1
So we ask, how many times can we divide n by 2 until we
reach 1?
That's solving:

n/2^k = 1
multiply both side by 2^k
n = 2^k
take log base 2
k = log n

That's why recursion depth = log n
Each level of recursion costs O(n)
e.g. merge step, at each level we merge subarrays
whose total size is n.
E.g. for n = 6:
(level 0)
[ 16 items ]  → merge cost = 16
(level 1)
[8 + 8 items] → merge cost = 16
(level 2)
[4+4+4+4] → merge cost = 16
(level 3)
[2+2+2+2+2+2+2+2] → merge cost = 16
(level 4)
[1 ... 1] → merge cost = 16

No matter how deep you go, every level costs O(n) work

Step 3: total work = (# levels) * work per level

work per level = n
num levels = log n
so total work T(n) = n * log(n)

Because the problem size halves each recursion, 
the recursion tree has log n levels, and 
because we do O(n) work at each level, the 
total work is O(n log n).
"""