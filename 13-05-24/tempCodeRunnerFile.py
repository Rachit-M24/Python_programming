
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_Integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        last = "I"
        sum = 0
        for numeral in s[::-1]:
            if roman_Integer[numeral] > roman_Integer[last]:
                sum += roman_Integer[numeral]
            else:
                sum -= roman_Integer[numeral]
                last = numeral
        return sum