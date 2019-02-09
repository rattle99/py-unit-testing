import unittest
import src.calc as calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(5,6), 11)
        self.assertEqual(calc.add(-5,50), 45)
        self.assertEqual(calc.add(-20,-6), -26)
        self.assertEqual(calc.add(19,6), 25)

    def test_subtract(self):
        self.assertEqual(calc.subtract(19,10), 9)
        self.assertEqual(calc.subtract(-19,10), -29)
        self.assertEqual(calc.subtract(19,-10), 29)
        self.assertEqual(calc.subtract(-19,-10), -9)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2,4), 8)
        self.assertEqual(calc.multiply(-2,4), -8)
        self.assertEqual(calc.multiply(2,-4), -8)
        self.assertEqual(calc.multiply(-2,-4), 8)
        self.assertEqual(calc.multiply(24,0), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(2,4), 0.5)
        self.assertEqual(calc.divide(4,-2), -2)
        self.assertEqual(calc.divide(23,0), "Error")
        self.assertEqual(calc.divide(-25,4), -6.25)

    def test_modulo(self):
        self.assertEqual(calc.modulo(2,4), 2)
        self.assertEqual(calc.modulo(10,3), 1)
        self.assertEqual(calc.modulo(23,0), "Error")

if __name__ == '__main__':
    unittest.main()
