import mulch

def test_less_than_5_cubic_yards():
    assert mulch.calculate_mulch_cost(3) == 108

def test_5_cubic_yards():
    assert mulch.calculate_mulch_cost(5) == 180

def test_greater_than_5_less_than_10_cubic_yards():
    assert mulch.calculate_mulch_cost(9) == 312

def test_10_cubic_yards():
    assert mulch.calculate_mulch_cost(10) == 345

def test_greater_than_10_cubic_yards():
    assert mulch.calculate_mulch_cost(11) == 375
