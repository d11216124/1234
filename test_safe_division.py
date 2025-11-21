"""
Unit tests for the safe_division module.
Tests include normal division, negative numbers, boundary values, and division by zero.
Unit Tests for Safe Division Module

This module contains comprehensive unit tests for the safe_division function.
Tests cover normal operations, edge cases, and error conditions.
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for safe_division function."""
    
    def test_normal_division(self):
        """Test normal division cases with positive numbers."""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(20, 4), 5.0)
        self.assertEqual(safe_division(100, 10), 10.0)
        self.assertEqual(safe_division(1, 2), 0.5)
    
    def test_negative_division(self):
        """Test division with negative numbers."""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
        self.assertEqual(safe_division(-100, 4), -25.0)
    
    def test_boundary_values(self):
        """Test division with boundary values."""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(1, 1), 1.0)
        self.assertAlmostEqual(safe_division(0.1, 0.1), 1.0)
        self.assertAlmostEqual(safe_division(1, 3), 0.3333333333333333)
    
    def test_division_by_zero(self):
        """Test division by zero is handled properly."""
        # This test expects None when dividing by zero
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(0, 0))
        self.assertIsNone(safe_division(-10, 0))
        self.assertIsNone(safe_division(100, 0))
    """Test cases for the safe_division function"""
    
    def test_basic_division(self):
        """Test basic division with positive integers"""
        result = safe_division(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_division_with_float(self):
        """Test division with floating point numbers"""
        result = safe_division(7.5, 2.5)
        self.assertEqual(result, 3.0)
    
    def test_division_by_zero(self):
        """Test that division by zero returns None"""
        result = safe_division(10, 0)
        self.assertIsNone(result)
    
    def test_zero_numerator(self):
        """Test division when numerator is zero"""
        result = safe_division(0, 5)
        self.assertEqual(result, 0.0)
    
    def test_negative_numbers(self):
        """Test division with negative numbers"""
        result = safe_division(-10, 2)
        self.assertEqual(result, -5.0)
        
        result = safe_division(10, -2)
        self.assertEqual(result, -5.0)
        
        result = safe_division(-10, -2)
        self.assertEqual(result, 5.0)
    
    def test_decimal_result(self):
        """Test division that results in a decimal"""
        result = safe_division(7, 3)
        self.assertAlmostEqual(result, 2.3333333333333335)
    
    def test_large_numbers(self):
        """Test division with large numbers"""
        result = safe_division(1000000, 1000)
        self.assertEqual(result, 1000.0)
    
    def test_small_numbers(self):
        """Test division with very small numbers"""
        result = safe_division(0.001, 0.01)
        self.assertAlmostEqual(result, 0.1)
    
    def test_invalid_numerator_type(self):
        """Test that TypeError is raised for invalid numerator type"""
        with self.assertRaises(TypeError):
            safe_division("10", 2)
    
    def test_invalid_denominator_type(self):
        """Test that TypeError is raised for invalid denominator type"""
        with self.assertRaises(TypeError):
            safe_division(10, "2")
    
    def test_invalid_both_types(self):
        """Test that TypeError is raised when both arguments are invalid"""
        with self.assertRaises(TypeError):
            safe_division("10", "2")
    
    def test_none_as_numerator(self):
        """Test that TypeError is raised when numerator is None"""
        with self.assertRaises(TypeError):
            safe_division(None, 2)
    
    def test_none_as_denominator(self):
        """Test that TypeError is raised when denominator is None"""
        with self.assertRaises(TypeError):
            safe_division(10, None)
    
    def test_list_as_argument(self):
        """Test that TypeError is raised when list is passed as argument"""
        with self.assertRaises(TypeError):
            safe_division([10], 2)
    
    def test_fractional_division(self):
        """Test division with fractions"""
        result = safe_division(1, 3)
        self.assertAlmostEqual(result, 0.3333333333333333)
    
    def test_one_divided_by_one(self):
        """Test the identity case: 1 / 1"""
        result = safe_division(1, 1)
        self.assertEqual(result, 1.0)
    
    def test_division_resulting_in_very_small_number(self):
        """Test division that results in a very small number"""
        result = safe_division(1, 1000000)
        self.assertEqual(result, 0.000001)


class TestSafeDivisionEdgeCases(unittest.TestCase):
    """Additional edge case tests for safe_division"""
    
    def test_float_zero_as_denominator(self):
        """Test division by float zero (0.0)"""
        result = safe_division(10, 0.0)
        self.assertIsNone(result)
    
    def test_negative_zero(self):
        """Test division by negative zero"""
        result = safe_division(10, -0.0)
        self.assertIsNone(result)
    
    def test_max_float_division(self):
        """Test division with very large float values"""
        result = safe_division(1e308, 1e2)
        self.assertAlmostEqual(result, 1e306)
    
    def test_min_float_division(self):
        """Test division with very small positive float values"""
        result = safe_division(1e-308, 1e2)
        self.assertAlmostEqual(result, 1e-310, places=15)


if __name__ == '__main__':
    unittest.main()
