class RomanNumeralGenerator(object):
 
    def generator(self, arabic):
        roman = self.to_roman(arabic)
        return roman
 
    def to_roman(self, number):
        roman_number = ""
        if (number == 5):
            roman_number = 'V'
        elif (number == 4):
            roman_number = 'IV'
        else:
            while (number > 0):
                roman_number += "I"
                number -= 1
        return roman_number
        
        
  