#!/usr/bin/env python3
"""
Demonstration of the safe_division function.
"""

from safe_division import safe_division


def main():
    """Demonstrate the safe_division function with various examples."""
    print("=== safe_division Function Demonstration ===\n")
    
    # Example 1: Normal division
    print("Example 1: Normal division")
    result = safe_division(10, 2)
    print(f"safe_division(10, 2) = {result}\n")
    
    # Example 2: Division by zero (prevented)
    print("Example 2: Division by zero (prevented)")
    result = safe_division(10, 0)
    print(f"safe_division(10, 0) = {result}")
    print("(Returns None to prevent division by zero error)\n")
    
    # Example 3: Float division
    print("Example 3: Float division")
    result = safe_division(7.5, 2.5)
    print(f"safe_division(7.5, 2.5) = {result}\n")
    
    # Example 4: Negative numbers
    print("Example 4: Negative numbers")
    result = safe_division(-10, 2)
    print(f"safe_division(-10, 2) = {result}\n")
    
    # Example 5: Using the result
    print("Example 5: Conditional usage")
    result = safe_division(100, 5)
    if result is not None:
        print(f"The result is: {result}")
    else:
        print("Division by zero prevented!")
    
    result = safe_division(100, 0)
    if result is not None:
        print(f"The result is: {result}")
    else:
        print("Division by zero prevented!")


if __name__ == "__main__":
    main()
