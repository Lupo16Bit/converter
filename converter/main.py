from Handler import Handler
from Converter import Converter
from ConverterTesting import ConverterTesting

""" 
    Konvertierung einer arabischen Zahl zur römischen Zahl.
    Zahl muss zwischen 0 und 5000 liegen. 
"""


handler = Handler()
conv = Converter()
convTest = ConverterTesting()
line = handler.line

while True:
        
        print('#'+ str(handler.cntr))
        number = input(" Eine Zahl von 1-4999 wählen:\n Arabische Ganzzahl:")
        
        handler.convert(number,conv,line)
        #handler.convertTestOnly(number, convTest, line)
        #handler.convertWithTest(number, conv, convTest, line)
        handler.cntr += 1
    
 