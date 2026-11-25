"""Write out a proof that sqrt(n) is irrational when n is not a perfect square.

Method: suppose sqrt(n) = a/b with gcd(a, b) = 1, so a^2 = n b^2. Pick a
prime p whose exponent in n is odd. In a^2 every prime has an even exponent.
In n b^2 the exponent of p is odd + even = odd. Unique factorisation makes
this impossible, so no such a/b exists.
"""
from math import isqrt


def factorise(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    out, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def is_perfect_square(n):
    return isqrt(n) ** 2 == n


def odd_prime(n):
    """The smallest prime that divides n to an odd power, or None."""
    for p, e in sorted(factorise(n).items()):
        if e % 2 == 1:
            return p
    return None


def prove(n):
    if n < 2:
        raise ValueError("n must be at least 2")
    p = odd_prime(n)
    if p is None:
        raise ValueError(f"{n} is a perfect square, so sqrt({n}) = {isqrt(n)} is rational")
    f = factorise(n)
    e = f[p]
    fac = " x ".join(f"{q}^{k}" if k > 1 else str(q) for q, k in sorted(f.items()))
    return [
        f"Claim: sqrt({n}) is irrational.",
        f"Suppose sqrt({n}) = a/b, where a and b are whole numbers with no common factor.",
        f"Squaring: a^2 = {n} b^2.",
        f"Factorise {n} = {fac}. The prime {p} appears {e} time(s), an odd number.",
        f"Every prime appears an even number of times in a^2, because a^2 = a x a.",
        f"In {n} b^2 the prime {p} appears {e} + (an even number) times, which is odd.",
        f"One number cannot have {p} an even number of times and an odd number of times.",
        f"So no such a and b exist, and sqrt({n}) is irrational.",
    ]


def no_small_solution(n, limit=500):
    """Exact check for the demo: no a, b <= limit with a^2 = n b^2."""
    for b in range(1, limit + 1):
        a2 = n * b * b
        if is_perfect_square(a2):
            return False
    return True
