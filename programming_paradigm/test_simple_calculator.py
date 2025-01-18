import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-6,-8), -14)
        # Add more assertions to thoroughly test the add method
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,4), 1)
        self.assertEqual(self.calc.subtract(10,-4), 14)
        self.assertEqual(self.calc.subtract(-5,1), -6)
        self.assertEqual(self.calc.subtract(-7,-4), -3)
        self.assertEqual(self.calc.subtract(0,4), -4)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6,4), 24)
        self.assertEqual(self.calc.multiply(-6,4), -24)
        self.assertEqual(self.calc.multiply(-6,-4), 24)
        self.assertEqual(self.calc.multiply(0,5), 0)
    def test_division(self):
        self.assertEqual(self.calc.divide(10,4), 2.5)
        self.assertEqual(self.calc.divide(16,-4), -4)
        self.assertEqual(self.calc.divide(-8,-2), 4)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
        
    
    
    
    
    
if __name__ == "__main__":
     unittest.main()
 







