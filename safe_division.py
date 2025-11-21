"""
Safe Division Module

This module provides a safe division function that handles division by zero
and other edge cases gracefully.
"""


def safe_division(numerator, denominator):
    """
    Safely divide two numbers with proper error handling.
    
    Args:
        numerator: The number to be divided (dividend)
        denominator: The number to divide by (divisor)
    
    Returns:
        The result of the division, or None if division by zero occurs
    
    Raises:
        TypeError: If inputs are not numeric types
from typing import Union, Optional


def safe_division(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """
    Safely divides two numbers, preventing division by zero.
    
    Args:
        a (int or float): The dividend (numerator)
        b (int or float): The divisor (denominator)
    
    Returns:
        float or None: The result of a / b if b is not zero, None if b is zero
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(7, 3)
        2.3333333333333335
    """
    # Type checking
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise TypeError("Both numerator and denominator must be numeric types (int or float)")
    
    # Handle division by zero
    if denominator == 0:
        return None
    
    # Perform the division
    return numerator / denominator
        >>> result = safe_division(10, 0)
        >>> result is None
        True
        >>> safe_division(7, 3)
        2.3333333333333335
    """
    if b == 0:
        return None
    return a / b
