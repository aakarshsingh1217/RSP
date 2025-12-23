"""
Given arrays A and B:
To compute the k-th number in the output, 
multiply A and B together in all possible
ways that add up to index k, and add those products.
Where vals outside array are treated as 0

Simple example
Let:
A = [2, 1, 3]   (length m = 3)
B = [4, 2]      (length n = 2)

Then C will have length:
(m + n – 1) = 3 + 2 – 1 = 4

So C = [C0, C1, C2, C3] 
we compute each C[k]:

We compute all A[j]·B[0–j]:
j=0: A[0] * B[0] = 2 * 4 = 8
j=1: A[1] * B[-1] = 1 * 0 = 0
j=2: A[2] * B[-2] = 3 * 0 = 0

C[0] = 8
"""