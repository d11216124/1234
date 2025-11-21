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
        >>> result = safe_division(10, 0)
        >>> result is None
        True
        >>> safe_division(7, 3)
        2.3333333333333335
    """
    if b == 0:
        return None
    return a / b
