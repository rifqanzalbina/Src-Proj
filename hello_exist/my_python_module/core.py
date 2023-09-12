# my_python_module/core.py

def greet(name):
    """
    This function takes a name as input and returns a greeting message.
    
    Parameters:
    name (str): The name of the person to greet
    
    Returns:
    str: A greeting message
    """
    if not isinstance(name, str):
        raise ValueError("The name should be a string")

    return f"Hello, {name}!"


def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
    a (int, float): The first number
    b (int, float): The second number
    
    Returns:
    int, float: The sum of the two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("The inputs should be numbers")

    return a + b


def subtract_numbers(a, b):
    """
    This function takes two numbers as input and returns their difference.
    
    Parameters:
    a (int, float): The first number
    b (int, float): The second number
    
    Returns:
    int, float: The difference between the two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("The inputs should be numbers")

    return a - b
