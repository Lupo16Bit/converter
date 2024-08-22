class Converter:
    def __init__(self):
        print("OBJ")        
    def convertIntToRoman(self, number):
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        outputRoman = ''
        i = 0
        while  number > 0:
            for _ in range(number // values[i]):
                outputRoman += symbols[i]
                number -= values[i]
            i += 1
        return outputRoman

    