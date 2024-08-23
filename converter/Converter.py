class Converter:
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
    def __init__(self):
        print("*** Converter erstellt ***")   

    def convertIntToRoman(self, number):

        outputRoman = ''
        i = 0
        
        if number > 0 and number <= 4999:
            while  number > 0:
                for _ in range(number // self.values[i]):
                    outputRoman += self.symbols[i]
                    number -= self.values[i]
                i += 1
            return " Römische Zahl: " + outputRoman
        else:
            print("Ungueltige Eingabe. Zahl muss im Bereich von 1 - 4999 liegen.")
        