# Tests for Fibonacci series.
from series import fibonacci

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

def test_fibonacci_negative_five():
    actual = fibonacci(-5)
    expected = "Invalid input"
    assert actual == expected

# Tests for Lucas numbers.
from series import lucas

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

def test_lucas_negative_ten():
    actual = lucas(-10)
    expected = "Invalid input"
    assert actual == expected

# Tests for sum_series
from series import sum_series

def test_sum_series_zero_no_optionals():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_zero_with_optionals():
    actual = sum_series(0, 5, 3)
    expected = 5
    assert actual == expected

def test_sum_series_five_with_optionals():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected

def test_sum_series_five_with_other_optionals():
    actual = sum_series(5, 4, 2)
    expected = 22
    assert actual == expected

def test_sum_series_with_negative_value():
    actual = sum_series(-5, 4, 2)
    expected = "Invalid input"
    assert actual == expected

def test_sum_series_with_negative_optionals():
    actual = sum_series(5, -4, -2)
    expected = -22
    assert actual == expected

def test_sum_series_with_mixed_optionals():
    actual = sum_series(8, -8, 3)
    expected = -41
    assert actual == expected