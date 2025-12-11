"""
Classical multiplication (O(n^2))

e.g.: multiply 9256 * 5367
old school method:

    9256
×   5367
-----------
   64792       (9256 × 7)
  555360       (9256 × 60)
 2776800       (9256 × 300)
46280000       (9256 × 5000)
-----------
 49677792

you're doing 4 * 4 digit multiplications -> 16 multiplications
each digit multiplication is constant time
Therefore cost is around n^2 for n digit numbers,
so standard multip is O(n^2)

NAIVE DIVIDE-AND-CONQUER MULTIPLICATION

Split each number into halves
e.g. suppose A = 1234 and B = 5678 
(4 digits -> n = 4 -> m = n / 2 = 2):
Split:
- A = 12(a1), 34(a0)
- B = 56(b1), 78(b0)
Represent:
A = a1 * 10^2 + a0, B = b1 * 10^2 + b0
Multiply:
A * B = a0b0 + (a0b1 + a1b0) * 10^2 + a1b1 * 10^4
^ to compute this you need:
a₀b₀

a₀b₁

a₁b₀

a₁b₁
That's 4 multiplications of size n/2
So recurrence is T(n) = 4T(n/2) + O(n)

Apply masters theorem:
- a = 4
- b = 2
- n^(log base 2 (4)) = n^2

f(n) = O(n), which is smaller, so case 1, result:
T(n) = theta(n^2)

KARATSUBA'S IMPROVEMENT: ONLY 3 MULTIPLICATIONS

You don't need all four a0b0 a0b1 a1b0 a1b1
You can reconstruct cross term using addition
instead of multiplication

E.g.: A = 1234, B = 5678

Split into halves:

a₀ = 34

a₁ = 12

b₀ = 78

b₁ = 56

Now compute only 3 products:

Karatsubas 3 multips:

q0 = a0b0 = 34 * 78 = 2652
q2 = a1b1 = 12 * 56 = 672
q1 = (a0 + a1)(b0 + b1) = 6164

Now use algebra:

a0b1 + a1b0 = q1 - q0 - q2 = 6164 - 2652 - 672 = 2840

therefore A * B = q0 + (q1-q0-q2)10^2 + q2*10^2
"""