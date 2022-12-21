from math_series.series import fibonacci, lucas, sum_series

#Tests fir fibonacci numbers


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_ten():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


# Tests for Lucas Numbers
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_ten():
    actual = lucas(10)
    expected = 123
    assert actual == expected


#Tests for sum_series


def test_one_sum_series_fibonacci():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_two_sum_series_lucas():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

