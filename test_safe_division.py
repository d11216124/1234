"""
Unit tests for the safe_division module.
Tests include normal division, negative numbers, boundary values, and division by zero.
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


if __name__ == '__main__':
    unittest.main()
