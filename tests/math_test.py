import pytest
from src.basic_calculator import add, divide, multiply, subtract

# Tests division functionality with positive integers.
def test_division():
    assert divide(1, 2) == 0.5
    
# Tests division by zero, expects to return an error message.
def test_division_zero():
    assert divide(1, 0) == "Error: Cannot divide by zero."
    
# Tests division functionality with a float as the divisor.
def test_division_float():
    assert divide(2, 0.5) == 4
    
    
# Tests addition functionality with positive integers.
def test_add():
    assert add(1, 2) == 3
    
# Tests addition functionality with floating point numbers.
def test_add_float():
    assert add(0.5, 0.7) == 1.2
    
# Tests addition functionality where one of the operands is negative.
def test_add_negative():
    assert add(2, -1) == 1
    
    
# Tests multiplication functionality with positive integers.
def test_multiply():
    assert multiply(1, 2) == 2
    
# Tests multiplication functionality with floating point numbers.
def test_multiply_float():
    assert multiply(0.5, 0.7) == 0.35
    
# Tests multiplication functionality where one of the operands is negative.
def test_multiply_negative():
    assert multiply(2, -1) == -2
    
    
# Tests subtraction functionality with positive integers.
def test_subtract():
    assert subtract(1, 2) == -1
    
# Tests subtraction functionality with floating point numbers, uses pytest.approx for precision issues.
def test_subtract_float():
    assert subtract(0.5, 0.7) == pytest.approx(-0.2)
    
# Tests subtraction functionality where one of the operands is negative.
def test_subtract_negative():
    assert subtract(2, -1) == 3
    
    
# Tests subtraction with invalid type inputs, expects to return an error message.
def test_subtract_type():
    assert subtract(1, "test") == "Error: Both arguments must be integers or floats."

# Tests addition with invalid type inputs, expects to return an error message.
def test_add_type():
    assert add(1, "test") == "Error: Both arguments must be integers or floats."
    
# Tests multiplication with invalid type inputs, expects to return an error message.
def test_multiply_type():
    assert multiply(1, "test") == "Error: Both arguments must be integers or floats."

# Tests division with invalid type inputs, expects to return an error message.
def test_divide_type():
    assert divide(1, "test") == "Error: Both arguments must be integers or floats."
