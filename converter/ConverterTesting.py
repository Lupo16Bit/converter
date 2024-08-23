from Converter import Converter

class ConverterTesting(Converter):
    def __init__(self):
        print("*** ConverterTesting erstellt ***")

    def convertIntToRoman(self, number):
        
        outputRoman = ''
        i = 0
        
        print("DEBUG   values[]:",self.values)
        print("DEBUG: symbols[]:",self.symbols)

        if number > 0 and number <= 4999:
            while  number > 0:
                for _ in range(number // self.values[i]):
                    print("DEBUG: number:",number," \t- values[i]:",self.values[i])
                    outputRoman += self.symbols[i]
                    number -= self.values[i]
                i += 1
            return "DEBUG: Roemische Zahl: " + outputRoman
    
        else:
            print("DEBUG: Ungueltige Eingabe. Zahl muss im Bereich von 1 - 4999 liegen.")
            
