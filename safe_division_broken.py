"""
Safe division module WITHOUT division by zero handling (for red light demonstration).
This version will cause tests to fail.
"""


def safe_division(a, b):
    """
    BROKEN VERSION: Division function without proper error handling.
    This version does NOT handle division by zero and will raise ZeroDivisionError.
    
    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)
    
    Returns:
        The result of a / b
    
    Raises:
        ZeroDivisionError: If b is zero (NOT HANDLED IN THIS VERSION)
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero
        >>> safe_division(-10, 2)
        -5.0
    """
    # Handle division by zero - COMMENTED OUT FOR RED LIGHT DEMO
    # if b == 0:
    #     return None
    return a / b
