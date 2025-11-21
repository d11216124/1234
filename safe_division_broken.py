"""
Safe division module WITHOUT division by zero handling (for red light demonstration).
This version will cause tests to fail.
"""


def safe_division(a, b):
    """
    Safely divide two numbers, handling division by zero.
    
    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)
    
    Returns:
        The result of a / b, or None if b is zero
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        >>> safe_division(-10, 2)
        -5.0
    """
    # Handle division by zero - COMMENTED OUT FOR RED LIGHT DEMO
    # if b == 0:
    #     return None
    return a / b
