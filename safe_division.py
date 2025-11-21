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
