from . import example_func


def test_example_func_str():
    assert example_func('a', 'b') == ('a', 'b')


def test_example_func_int():
    assert example_func(1, 2) == (1, 2)


def test_example_func_float():
    assert example_func(42.0, 15.0) == (42., 15.)


