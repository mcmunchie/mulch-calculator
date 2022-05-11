import pytest
import mulch

# Elements of input_values corresponds to length, width and depth

def test_cubic_yards_is_5():
    input_values = [30, 9, 6]
    mulch.input = lambda _: input_values.pop(0)

    assert mulch.get_cubic_yards() == 5.0

def test_cubic_yards_returns_fraction():
    input_values = [30, 6, 6]
    mulch.input = lambda _: input_values.pop(0)

    assert mulch.get_cubic_yards() == pytest.approx(3.333, rel=3e-3)

def test_cubic_yards_is_1():
    input_values = [27, 1, 12]
    mulch.input = lambda _: input_values.pop(0)

    assert mulch.get_cubic_yards() == 1.0
