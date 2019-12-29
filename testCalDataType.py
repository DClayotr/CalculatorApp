#unit test for calDataType.py

import unittest
from CalDataType import calculate

class TestCalculate(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate('+',3,4), 7)

    def test_sub(self):
        self.assertEqual(calculate('-',4,3), 1)

    def test_mult(self):
        self.assertEqual(calculate('*',3,4),12)

    def test_div(self):
        self.assertAlmostEqual(calculate('/',4,5),0.8)
        
    def test_expo(self):
        self.assertEqual(calculate('^',3,2), 9)


