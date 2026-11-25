# irrationality-proof-builder

Writes out a step by step proof that the square root of a non-square whole number is irrational.

## What it solves
Students learn the proof for sqrt(2) and then meet sqrt(12) or sqrt(75) and do not know how to adapt it. This tool picks the right prime for any non-square n and writes the proof in numbered steps; perfect squares are refused with the reason. Pure Python 3.10+, standard library only.

## Example
```bash
python -m irrproof 12
```
```
1. Claim: sqrt(12) is irrational.
2. Suppose sqrt(12) = a/b, where a and b are positive whole numbers.
3. Squaring: a^2 = 12 b^2.
4. Factorise 12 = 2^2 x 3. The prime 3 appears 1 time(s), an odd number.
5. Write a = p1^e1 x ... x pk^ek (its prime factorisation). Then a^2 = p1^(2 e1) x ... x pk^(2 ek), so every prime in a^2 has an even exponent. The same argument shows every prime in b^2 has an even exponent.
6. On the right side, 12 b^2 has the prime 3 with exponent 1 + (an even number), and odd + even is odd. So the exponent of 3 is odd on the right.
7. On the left side, a^2 has the prime 3 with an even exponent (possibly 0).
8. The two sides are the same number, but unique factorisation says a number has exactly one exponent for 3. It cannot be both even and odd. This is a contradiction.
9. So no such a and b exist, and sqrt(12) is irrational.
```
The reason in step 5 is the real one: writing a as a product of prime powers and squaring doubles every exponent, so every prime in a^2 (and in b^2) has an even exponent. The prime with an odd exponent in n then has an odd exponent on the left side of n b^2 = a^2 and an even one on the right, which unique factorisation forbids.

## What it refuses, and why
```bash
python -m irrproof 1
python -m irrproof 0
python -m irrproof -4
python -m irrproof 49
```
```
error: 1 = 1^2 is a perfect square, so sqrt(1) = 1 is rational
error: 0 = 0^2 is a perfect square, so sqrt(0) = 0 is rational
error: -4 is negative, so it has no real square root and there is nothing to prove
error: 49 is a perfect square, so sqrt(49) = 7 is rational
```
- 1 = 1^2 is a perfect square, so sqrt(1) = 1 is rational. The same holds for every perfect square (and 0 = 0^2).
- Negative numbers have no real square root, so there is nothing to prove.
(Output pasted from real runs.)

## The maths behind it
Suppose sqrt(n) = a/b with a and b positive whole numbers. Then a^2 = n b^2. If a = p1^e1 ... pk^ek then a^2 = p1^(2 e1) ... pk^(2 ek), so every exponent in a^2 is even; the same holds for b^2. If n is not a perfect square, some prime p has an odd exponent in n, so p has an odd exponent in n b^2 (odd plus even), but an even one in a^2. Unique factorisation says the exponent of p is the same on both sides, which is a contradiction. The tool also has an exact check, used in the tests, that finds no a, b up to 500 with a^2 = n b^2 for non-squares.

## Install and run
```bash
python -m pip install -e .
python -m pytest
```

## Licence
MIT. Made by Math & Myth (mathandmyth.ae): one to one maths mentoring, online, across the UAE.
