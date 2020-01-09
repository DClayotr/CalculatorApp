#unit Test for EqParse function
import unittest
from EqIterator import eqIterator
from EqParse import EqParse

class TestEquationParse(unittest.TestCase):

    def test_EQ(self):
        equation = EqParse("1+(9/(~1+2))")

        self.assertEqual(eqIterator(equation), 10)

    @unittest.expectedFailure
    def test2(self):
        equation = EqParse("(9*7)+(5+6)")

        self.assertEqual(eqIterator(equation), 74)
