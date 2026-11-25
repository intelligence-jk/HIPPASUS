"""Write out a proof that sqrt(n) is irrational when n is not a perfect square.

Method: suppose sqrt(n) = a/b with a, b positive whole numbers, so a^2 = n b^2. Pick a
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
    if n < 0:
        raise ValueError(f"{n} is negative, so it has no real square root and there is nothing to prove")
    if n == 0:
        raise ValueError("0 = 0^2 is a perfect square, so sqrt(0) = 0 is rational")
    if n == 1:
        raise ValueError("1 = 1^2 is a perfect square, so sqrt(1) = 1 is rational")
    p = odd_prime(n)
    if p is None:
        raise ValueError(f"{n} is a perfect square, so sqrt({n}) = {isqrt(n)} is rational")
    f = factorise(n)
    e = f[p]
    fac = " x ".join(f"{q}^{k}" if k > 1 else str(q) for q, k in sorted(f.items()))
    return [
        f"Claim: sqrt({n}) is irrational.",
        f"Suppose sqrt({n}) = a/b, where a and b are positive whole numbers.",
        f"Squaring: a^2 = {n} b^2.",
        f"Factorise {n} = {fac}. The prime {p} appears {e} time(s), an odd number.",
        "Write a = p1^e1 x ... x pk^ek (its prime factorisation). Then a^2 = p1^(2 e1) x ... x pk^(2 ek), "
        "so every prime in a^2 has an even exponent. The same argument shows every prime in b^2 has an even exponent.",
        f"On the right side, {n} b^2 has the prime {p} with exponent {e} + (an even number), "
        "and odd + even is odd. So the exponent of "
        f"{p} is odd on the right.",
        f"On the left side, a^2 has the prime {p} with an even exponent (possibly 0).",
        f"The two sides are the same number, but unique factorisation says a number has exactly one exponent for {p}. "
        "It cannot be both even and odd. This is a contradiction.",
        f"So no such a and b exist, and sqrt({n}) is irrational.",
    ]


def no_small_solution(n, limit=500):
    """Exact check for the demo: no a, b <= limit with a^2 = n b^2."""
    for b in range(1, limit + 1):
        a2 = n * b * b
        if is_perfect_square(a2):
            return False
    return True
