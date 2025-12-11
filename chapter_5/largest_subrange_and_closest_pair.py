"""
Suppose you are tasked with writing the advertising copy for a 
hedge fund whose
monthly performance this year was
[−17, 5, 3, −10, 6, 1, 4, −3, 8, 1, −13, 4]

Largest subrange prob takes array A of n nums, and asks for index
pair i and j that maximises the sum. Summing entire array doesn't
maximise S because of negative numbers. Explicitly testing
each possible interval start end pair requires Ω(n^2) time.
Can use divide and conquer instead

Divide array A into left and right halves, where can largest sub-
range be? either in left or right half, or includes middle.
A recursive program to find the largest subrange between A[l]
and A[r] can easily call itself to work on left and right
subproblems. How can we find largest subrange spanning middle,
that is, spanning position m and m + 1?

Key's to observe largest subrange centered spanning middle
will be union of largest subrange on left ending on m
and largest subrange on right starting from m + 1
"""

"""
What is the Largest Subrange Problem?

Given array A, find indices i and j such that:
the sum between i and j is as large as possible,
where subrange must be contiguous.
Negative numbers matter (might reduce sum)

2. Example Array (Hedge Fund Monthly Gains)
Index:   1   2  3   4   5  6  7   8   9  10  11 12
A =    [-17, 5, 3, -10, 6, 1, 4, -3, 8, 1, -13, 4]

Best performing period is May -> Oct (indices 5 - 10)
6 + 1 + 4 - 3 + 8 + 1 = 17

So max subarray sum is:
i = 5
j = 10
S = 17

Why brute force takes Ω(n²)
There are:
n choices for start index i
n choices for end index j
total: n^2 subarrays to test
Even just touching each subarray once -> Omega(n^2)

Divide–and–Conquer Algorithm (O(n log n))

Max subarray must be one of these:
entirely in left half
entirely in right half
straddling middle (starts left, ends right)
(exactly like mergesort logic)
(this is because every subarray in entire arr must fall into
either left, right, or straddling middle)

How do we handle the “straddling the middle” case?

Let the array range be from l → r with midpoint m.
 Left half:  A[l ... m]
 Right half: A[m+1 ... r]

To find largest subarray crossing middle,
find best suabrray ending exactly at m:
sweep left -> accumulate partial sums -> keep max
find best subarray starting exactly at m + 1:
sweep right -> accumulate partial sums -> keep max
add them together:
this gives best crossing middle subarray

Example — Step Through Your Array (Small Version)
A = [2, -1, 3, -4, 5]

Split:
Left:  [2, -1, 3]
Right: [-4, 5]
m = 3

Step A — Solve left half recursively
Max subarray is [2, -1, 3] → sum = 4

Step B — Solve right half recursively
Max subarray is [5] → sum = 5

Step C — Solve straddling middle
Largest subarray ending at m (index 3):
3 → sum = 3
-1 + 3 → sum = 2
2 -1 + 3 → sum = 4  (best)
Largest subarray starting at m+1 (index 4):
-4 → sum = -4
-4 + 5 → sum = 1  (best)
Crossing sum = 4 + 1 = 5

Final choice:

Left max = 4

Right max = 5

Crossing max = 5

So overall answer = 5.
"""