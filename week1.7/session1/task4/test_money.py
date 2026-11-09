# test_money.py
import pytest
from money import Money

def test_invalid_type_pound():
    with pytest.raises(TypeError) as excinfo:
        Money(1.2, 99)
    assert str(excinfo.value) == "pounds must be an integer"

def test_invalid_value_pound():
    with pytest.raises(ValueError) as excinfo:
        Money(-1, 0)
    assert str(excinfo.value) == "pounds must be >= 0"

def test_add_invalid_type():
    m1 = Money(5, 0)
    with pytest.raises(TypeError) as excinfo:
        m1 + 42
    assert str(excinfo.value) == "other object must be a Money"

def test_invalid_type_pence():
    with pytest.raises(TypeError) as excinfo:
        Money(1, "99")
    assert str(excinfo.value) == "pence must be an integer"

def test_invalid_value_pence():
    with pytest.raises(ValueError) as excinfo:
        Money(1, -1)
    assert str(excinfo.value) == "pence must be >= 0"

def test_valid_add():
    m1 = Money(1, 50)
    m2 = Money(0, 75)
    result = m1 + m2
    assert str(result) == "£2.25"
