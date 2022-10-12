from re import X


class RomanNumeralGenerator:
    def generator(self, arabic):
        roman = self.number_to_numeral(arabic)
        return roman

    def to_roman(self, x):
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        roman_numeral = ""
        while x != 0:
            if numbers[i] <= x:
                roman_numeral += roman[i]
                x = x - numbers[i]
            else:
                i -= 1
        return roman_numeral

    # Alternative method...

    def number_to_numeral(self, number):

        numerals_dict = {
            "ones": ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            "tens": ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            "hundreds": ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            "thousands": ["", "M", "MM", "MMM"],
        }
        bases = ["ones", "tens", "hundreds", "thousands"]
        s = []
        for base in bases:
            number, remainder = divmod(number, 10)
            s.insert(0, numerals_dict[base][remainder])
        return "".join(s)


test_dict = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
}
