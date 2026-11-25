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
    assert "a x a" not in " ".join(steps)
    assert "p1^(2 e1)" in steps[4] and "unique factorisation" in steps[7]
    assert steps[-1].endswith("irrational.")


def test_prove_rejects_square():
    with pytest.raises(ValueError):
        prove(49)
    with pytest.raises(ValueError):
        prove(1)


@pytest.mark.parametrize("n,word", [(1, "1^2"), (0, "0^2"), (-4, "negative"), (-1, "no real square root")])
def test_refusal_reasons(n, word):
    with pytest.raises(ValueError) as e:
        prove(n)
    assert word in str(e.value)


def test_one_message_matches_readme():
    with pytest.raises(ValueError) as e:
        prove(1)
    assert "rational" in str(e.value)
    assert "1 = 1^2 is a perfect square" in open("README.md").read()


@pytest.mark.parametrize("n", [2, 3, 5, 8, 12, 75])
def test_prove_has_real_reason(n):
    text = "\n".join(prove(n))
    assert "a^2 = p1^(2 e1)" in text and "even exponent" in text and "unique factorisation" in text


def test_no_small_solution_for_non_squares_only():
    assert no_small_solution(2) and no_small_solution(12) and no_small_solution(75)
    assert not no_small_solution(16)


def test_bad_factorise():
    with pytest.raises(ValueError):
        factorise(0)
