from src.numbers import sum_even_numbers


def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4, 5]) == 6
    assert sum_even_numbers([10, 15, 20, 25]) == 30
    assert sum_even_numbers([-2, -1, 0, 1, 2]) == 0
    assert sum_even_numbers([]) == 0
