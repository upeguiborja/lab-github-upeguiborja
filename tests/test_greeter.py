import pytest
from src.greeter import greet

def test_greet_default():
    assert greet("don Ramon") == "Hola, don Ramon!"

def test_greet_morning():
    assert greet("don Ramon", 8) == "Buenos días, don Ramon."

def test_greet_afternoon():
    assert greet("don Ramon", 15) == "Buenas tardes, don Ramon."

def test_greet_night():
    assert greet("don Ramon", 22) == "Buenas noches, don Ramon."

def test_invalid_hour():
    with pytest.raises(ValueError):
        greet("don Ramon", 25)

def test_empty_name():
    with pytest.raises(ValueError):
        greet("", 10)

