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
2. Suppose sqrt(12) = a/b, where a and b are whole numbers with no common factor.
3. Squaring: a^2 = 12 b^2.
4. Factorise 12 = 2^2 x 3. The prime 3 appears 1 time(s), an odd number.
5. Every prime appears an even number of times in a^2, because a^2 = a x a.
6. In 12 b^2 the prime 3 appears 1 + (an even number) times, which is odd.
7. One number cannot have 3 an even number of times and an odd number of times.
8. So no such a and b exist, and sqrt(12) is irrational.
```
(Output pasted from a real run.)

## The maths behind it
Suppose sqrt(n) = a/b with a and b whole numbers with no common factor. Then a^2 = n b^2. In a^2 every prime has an even exponent. If n is not a perfect square, some prime p has an odd exponent in n, so p has an odd exponent in n b^2 (odd plus even). Unique factorisation says the exponent of p in a^2 and in n b^2 must agree, which is a contradiction. The tool also has an exact check, used in the tests, that finds no a, b up to 500 with a^2 = n b^2 for non-squares.

## Install and run
```bash
python -m pip install -e .
python -m pytest
```

## Licence
MIT. Made by Math & Myth (mathandmyth.ae): one to one maths mentoring, online, across the UAE.
