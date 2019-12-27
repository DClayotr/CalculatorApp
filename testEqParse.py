#unit Test for EqParse function
import unittest
from EqParse import EqParse

class TestEquationParse(unittest.TestCase):

    def test_EQ(self):
        eqTestArr = [716565.583,'/','(',82156,'*',6554,'-',2222,')']
        self.assertEqual(EqParse("716565.583/.//(82156*6554-2222)"), eqTestArr) 