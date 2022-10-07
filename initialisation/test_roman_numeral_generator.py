import unittest
from initialisation.roman_numeral_generator import RomanNumeralGenerator

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
 
if __name__ == '__main__':
    unittest.main()