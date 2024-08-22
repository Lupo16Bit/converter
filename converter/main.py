from Converter import Converter 
from ConverterTesting import ConverterTesting
number = input("Zahl zwischen 0 und 4999 eingeben: ")
outln = ""

conv = Converter()
print("MARK")
print(conv.convertIntToRoman(int(number)))
conv2 = ConverterTesting()
print(conv2.convertIntToRoman(int(number)))
print("DONE")
