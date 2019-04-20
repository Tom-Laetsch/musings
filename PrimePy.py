import numpy as np
import time

"""
A brute force method of creating an sequence of primes would go as follows:
- Start with an initial list of consecutive primes.
- Iterate through consecutive integers starting at the first integer bigger than the largest element in the list.
- Continue iterating until we land on one which is not divisible by any of the primes in list
- Once this happens, that integer must be prime. Append that number to the list and restart with the appended list.
WHY NOT USE THIS METHOD?? It's not efficient. We end up checking many more divisions than we need to.

After some thought, it turns out one way to make this more efficient is to observe that to test if a number x
is prime, we only need to check that it is not divisible by primes less than or equal to the square root of x.
This becomes obvious when you ask, what if no prime p <= sqrt(x) has the property that x%p == 0.
Then, if x were not prime there would need to be at least two prime numbers p1, p2 with sqrt(x) < p1,p2 < x
with p1*p2 <= x, but p1*p2 > sqrt(x)^2... Another way to think of this is that if p is the smallest prime < x,
then x must be at least p^2 since all prime factors of x are at least size p, and with p < x, it must that
there are at least two prime factors.

This observation is used in the functions below, with some proofs for why we expect them to work.
"""

"""
Lemma:
Suppose that p_0 = 2, p_1 = 3, ..., p_n are the first n+1 consecutive primes. If any number x
(1) p_i does not divide x for 0 <= i <= n
(2) x <= p_n^2
then x is prime.

Proof:
Suppose that (1) holds and suppose that p is the smallest prime that divides x (including the possibility that p = x). By (1), we know that p > p_n.
If p != x, then there is another prime q >= p such that q divides x, and hence p*q <= x; this implies that p_n^2 < x since p_n < p <= q. This shows
us that either p = x, or x > p_n^2. Hence by the assumption of (2), p = x and therefore x is prime.
"""
def prime_seq_gen( maxval, start_seq = [2,3,5,7,11,13] ):
    pseq = start_seq
    largest = pseq[-1]
    for x in range( largest+2, maxval + 1, 2 ):
        for p in pseq[1:]:
            if (x%p == 0):
                # x is not prime
                break
            else:
                if x < p**2:
                    # by lemma, x is prime
                    pseq.append( x )
                    break
    return pseq

"""
Lemma:
If x is any positive integer such that no prime p less than or equal to sqrt(x) divides x, then x is prime.

Proof:
If the hypotheses of the Lemma hold, then if p is the smallest prime dividing x, it must be that p > sqrt(x). Hence, if any other prime, q,
we have x=sqrt(x)^2 < p*q <= x, a contradiction; thus there is no other prime q, and hence p = x.
"""
def is_prime( val ):
    start_seq = [2,3,5,7,11,13]
    if val in start_seq:
        return True
    for p in start_seq:
        if (val%p == 0):
            print( "%d = %d * %d" % (val, p, val // p) )
            return False
    sqv = int( np.ceil( np.sqrt( val ) ) )
    if sqv <= start_seq[-1]:
        return True

    lss = len( start_seq )
    pseq = prime_seq_gen( maxval = sqv, start_seq = start_seq )
    for p in pseq[lss:]:
        if (val%p == 0):
            print( "%d = %d * %d" % (val, p, val // p) )
            return False
    return True
