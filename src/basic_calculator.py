def add(a, b):
    """Function to add two numbers."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Error: Both arguments must be integers or floats."
    return a + b

def subtract(a, b):
    """Function to subtract two numbers."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Error: Both arguments must be integers or floats."
    return a - b

def multiply(a, b):
    """Function to multiply two numbers."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Error: Both arguments must be integers or floats."
    return a * b

def divide(a, b):
    """Function to divide two numbers."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Error: Both arguments must be integers or floats."
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


