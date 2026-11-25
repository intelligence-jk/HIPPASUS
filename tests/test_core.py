import pytest
from irrproof import factorise, odd_prime, is_perfect_square, prove, no_small_solution


def test_factorise():
    assert factorise(360) == {2: 3, 3: 2, 5: 1}
    assert factorise(1) == {}


def test_factorise_product_matches():
    for n in range(1, 300):
        prod = 1
        for p, e in factorise(n).items():
            prod *= p ** e
        assert prod == n


def test_perfect_squares():
    assert is_perfect_square(144) and not is_perfect_square(143)


def test_odd_prime():
    assert odd_prime(12) == 3
    assert odd_prime(2) == 2
    assert odd_prime(36) is None


def test_odd_prime_agrees_with_squareness():
    for n in range(2, 400):
        assert (odd_prime(n) is None) == is_perfect_square(n)


def test_prove_text():
    steps = prove(12)
    assert "3" in steps[3] and "a^2 = 12 b^2" in steps[2]
    assert steps[-1].endswith("irrational.")


def test_prove_rejects_square():
    with pytest.raises(ValueError):
        prove(49)
    with pytest.raises(ValueError):
        prove(1)


def test_no_small_solution_for_non_squares_only():
    assert no_small_solution(2) and no_small_solution(12) and no_small_solution(75)
    assert not no_small_solution(16)


def test_bad_factorise():
    with pytest.raises(ValueError):
        factorise(0)
