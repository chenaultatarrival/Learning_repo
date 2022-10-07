class RomanNumeralGenerator(object):
 
    def generator(self, arabic):
        roman = self.to_roman(arabic)
        return roman
 
    def to_roman(self, number):
        if(number == 1):
            return('I')
        else:
            return('II')    