
class Handler:

    cntr = 0
    line = "-------------------------------------------------------------"

    def __init__(self):
        "Handler erstellt"
    # Convert Solo
    def convert(self,number, Converter,line):
        print(Converter.convertIntToRoman(int(number)))
        print(line)

    # ConvertTesting Solo
    def convertTestOnly(self,number,ConverterTesting,line):
        print(ConverterTesting.convertIntToRoman(int(number)))
        print(line)

    # Convert && ConvertTesting
    def convertWithTest(self,number, Converter, ConverterTesting, line):
            print(Converter.convertIntToRoman(int(number)))
            print(line)

            print(ConverterTesting.convertIntToRoman(int(number)))
            print(line)
