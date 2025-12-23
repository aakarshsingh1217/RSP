"""
Las vegas algorithms: randomized algs guarantee correctness,
and're usually efficient (not always), e.g. Quicksort

Monte Carlo algorithms: randomized algs are probably
efficient and usually (but not always) produce the
correct answer or something close it. e.g. random 
sampling methods
"""

"""
Why is randomized quicksort las vegas alg, and not monte
carlo

Monte Carlo algs are always fast and usually correct,
while Las Vegas algs are always correct and usually
fast.
Randomized quicksort always prods a sorted permutation,
so we know it's always correct. Picking a very bad
series of pivots might cause the running to exceed O(nlogn),
but we're always going to end up sorted, therefore quicksort
is Las Vegas alg.
"""

"""
an experiment is a procedure that yields one of a set of
possible outcomes. as our ongoing examples, consider experim
of tossing two six sided dice, one red and one blue, with
each face bearing a distinct integer {1, ..., 6}

sample space S is the set of possible outcomes for our experiment,
in our dice example, there're 36 possible outcomes:

S = {(1, 1),(1, 2),(1, 3),(1, 4),(1, 5),(1, 6),
(2, 1),(2, 2),(2, 3),(2, 4),(2, 5),(2, 6),
(3, 1),(3, 2),(3, 3),(3, 4),(3, 5),(3, 6),
(4, 1),(4, 2),(4, 3),(4, 4),(4, 5),(4, 6),
(5, 1),(5, 2),(5, 3),(5, 4),(5, 5),(5, 6),
(6, 1),(6, 2),(6, 3),(6, 4),(6, 5),(6, 6)}.

event E is a specified subset of the outcomes of an
experiment. Even that the sum of the dice equals 7 and 11
(conditions to win at craps) is subset:

E = {(1, 6),(2, 5),(3, 4),(4, 3),(5, 2),(6, 1),(5, 6),(6, 5)}.

Probability of an outcome s, denoted p(s), is number with two
properties:

- for each outcome s in sample space S, 0 <= p(s) <= 1
- sum of probabilities of all outcomes adds to 1

if we assume two distinct fair dice, probability 
p(s) = 1/6 * 1/6 = 1 / 36 for all outcomes s in the set of S

Probability of event E is sum of probabilities of outcome
of event, or complement of event E where E does not occur,
e.g. P(E) = 1 - P(E)

random var V is a numerical func on outcomes of a probability
space. the func "sum vals of two dice" (v((a, b)) = a + b)
prods an integer result between 2 and 12. This implies a
probability distr of possible vals of random var.
Probability P(V(s) = 7) = 1/6, while P(V(s) = 12) - 1/36

When you roll two six-sided dice, the outcome is a pair:
(a, b)

where:
a = val on die 1
b = val on die 2
each ranges from 1 to 6

So sample space (all possible outcomes) is:
S = {(1, 1), (1, 2), ..., (6, 6)} (36 equally likely outcomes)

A random variable is just a func that assigns a num to each
outcome.
here:
    V(a, b) = a + b

    random var is sum of vals on two dice.

    e.g. V(1, 1) = 1 + 1 = 2
    v(3, 4) = 7

Even though outcomes are pairs, random var
outputs a single num

We want probability P(V = k)

E.g., prob sum is 7:

list all pairs (a, b) where a + b = 7

(1,6)
(2,5)
(3,4)
(4,3)
(5,2)
(6,1)

6 outcomes, total 36 outcomes

therefore, P(V = 7) = 6/36 = 1/6

Expected value of a random variable V defined on
sample space S, E(V), is defined as multiplying
each possible outcome by its probability, then adding
them all up

e.g. sum of two dice V(a, b) = a+b

2 happens with prob 1/36,
3 happens with 2/36
...
12 happens with prob 1 / 36

E(V) = k = 2 to 12 (k * P(V = k))

E(V) = 2*(1/36)
     + 3*(2/36)
     + 4*(3/36)
     + 5*(4/36)
     + 6*(5/36)
     + 7*(6/36)
     + 8*(5/36)
     + 9*(4/36)
     + 10*(3/36)
     + 11*(2/36)
     + 12*(1/36)

so E(V) = 7
"""

"""
Can get complex events computed from simpler events
A and B on same set of outcomes.

Perhaps event A is that at least one of two dice
be an even number, while event B denotes rolling
either 7 or 11. Note that there's outcomes of A
that're not outcomes of B, specifically

A − B = {(1, 2),(1, 4),(2, 1),(2, 2),(2, 3),
(2, 4),(2, 6),(3, 2),(3, 6),(4, 1),
(4, 2),(4, 4),(4, 5),(4, 6),(5, 4),(6, 2),(6, 3),(6, 4),(6, 6)}

This is the set diff oper, B - A = {} because every pair
adding to 7 or 11 must contain one odd and one even
num.
Outcomes in common between both events A and B are
called the intersection, denoted A ∩ B, written as:

A ∩ B = A − (S − B)

outcomes that appear in either A or B are called the union
denoted A ∪ B, probability of union and intersection
are related by formula:
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

With complement oper. A = S - A, we get right language
for combining events. Therefore, we can readily
compute probability of any of these sets by summing probabilities
of outcomes in defined sets.

Events A and B are said to be independent if:
P(A ∩ B) = P(A) × P(B)
This means there's no special structure of outcomes
shared between events A and B. Assuming half of the
students in my class are female, and half students in my
class are above average, we'd expect that a quarter of my
students are both female and above average if events
independent.

Probability theorists love independent events, because
it simplifies their calcs. E.g., if A subscript i denotes
denotes event of getting an even num on the ith dice
throw, then probability of obtaining all evens in a throw
of two dice is P(A1 ∩ A2) = P(A1)P(A2) = (1/2)(1/2) = 1/4.
Then, probability of A, that at least one of two dice is
P(A) = P(A1 ∪ A2) = P(A1) + P(A2) − P(A1 ∩ A2)=1/2+1/2 − 1/4=3/4

Presuming that P(B) > 0, conditional probability of A given
B, P(A|B), is defined as
P(A|B) = P(A ∩ B) / P(B)

in particular, if events A and B are independent, then

P(A|B) = P(A)P(B)/P(B) = P(A)

and B has no impact on likelihood of A.

Conditional probability becomes interesting only when
two events have dependence on each other. Recall
dice rolling events, namely:
• Event A: at least one of two dice is an even number.
• Event B: the sum of the two dice is either 7 or 11

Observe P(A|B) = 1, because any roll summing to an
odd val must consist of one even and one odd.
Thus, A ∩ B = B. For  For P(B|A), note P(A ∩ B) = P(B)=8/36,
and P(A) = 27/36, so P(B|A)=8/27.

Our primary tool to compute conditional probabilities will be 
Bayes’ theorem, which reverses the direction of the dependencies:

P(B|A) = P(A|B)P(B) / P(A)

Central tendency measures capture the center around which
the random samples or data points are distributed.
Variation measures the spread, that is, how far
the random samples or data points lie from the center.

Primary centrality measure is the mean, mean of a random
var V, denoted E(V) (expected value) is given by:
E(V) = V(s)p(s)

When elementary events are all of equal prob, mean or avg
computed as:
X = (add up all vals and divide by how many there are)

Most common measure of variabiliyt is standard deviation.
Variance is the square of standard deviation.
"""

"""
Ball and bin problems are classics of probability theory.
We're given x identical balls to toss at random
with y labeled bins. We're interested in the resulting
distribution of balls. How many bins expected
to contain a given number of balls?

Hashing can be thought of as a ball and bin process. Suppose
we hash n balls/keys into n bins/buckets. We expect an
average of one ball per bin, but note that this'll be
true regardless of how good or bad hash func is.
"""

"""
Even though a hash function is determinstic, good hash
functions scatter keys as if they were random.

E.g. Suppose we hash strings by summing ASCII values and 
taking mod 10.
h("cat") = 312 mod 10 = 2
h("dog") = 314 mod 10 = 4
h("bird") = 412 mod 10 = 2
The outputs look random, even though they are 100% deterministic.

BUT THIS CAUSES A PROBLEM

Since the hash function is fixed and deterministic, 
an attacker can deliberately craft keys that collide.

Assume your hash table has 10 buckets (0–9):
bucket 5: ----> A, B, C, D, E, F, G, H, ...
If someone finds many keys whose hash 
value = 5, every lookup becomes O(n) instead of O(1).

This is possible because:
Any deterministic hash function has a worst-case input.

If you hash 1000 keys into 10 buckets, 
some bucket must contain at least 100 keys.

How Randomizing the Hash Function Fixes This
We remove the attacker’s advantage by 
choosing the hash function randomly from a 
family of hash functions.

The input cannot be chosen to defeat our hash function, 
because the hash function wasn’t known when the input was created.

Expected lookup time becomes O(1) for any input.

The book describes defining a hash function like:
h(x) = (f(x) mod p) mod m
where:
m = size of hash table

p = a random large prime

f(x) = some integer representation of key x

Why does this make hashing randomized
Because different choices of p give completely 
different hashing behavior.

Let’s use:
m = 17 (17 buckets)
key numeric value f(x) = 21347895537127

Try two different p values:
Case 1: No reduction
h(x) = 21347895537127 mod 17 = 8

Case 2: Use random p = 2342343
f(x) mod p = 21347895537127 mod 2342343 = 2175935
h(x) = 2175935 mod 17 = 12

Same key → two completely different buckets 
depending on random choice of p.
"""