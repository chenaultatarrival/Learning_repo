import unittest
import pytest
from initialisation.roman_numeral_generator import RomanNumeralGenerator

#@pytest.mark.parametrize("test_input,expected", [(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')])
#def test_eval(test_input, expected):
#    RomanNumeralGenerator.generator(test_input)
#    assert eval(test_input) == expected

class RomanNumeralTestCase(unittest.TestCase):
    # Tests for `roman_numeral_generator.py`
 
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.testclass = RomanNumeralGenerator()
 
    def tearDown(self):
        unittest.TestCase.tearDown(self)
 
    def test_one(self):
        # Does 1 return I? 
        result = self.testclass.generator(1)
        self.assertEqual(result, 'I')

    def test_two(self):
        result = self.testclass.generator(2)
        self.assertEqual(result, 'II')

    def test_three(self):
        result = self.testclass.generator(3)
        self.assertEqual(result, 'III')

    def test_four(self):
        result = self.testclass.generator(4)
        self.assertEqual(result, 'IV')
    
    def test_five(self):
        result = self.testclass.generator(5)
        self.assertEqual(result, 'V')
    
    def test_six(self):
        result = self.testclass.generator(6)
        self.assertEqual(result, 'VI')

    
 
if __name__ == '__main__':
    unittest.main()