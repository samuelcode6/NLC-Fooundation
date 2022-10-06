#!/bin/usr/python3
'''python
'''
m = "Programming is like building a multilingual puzzle"

#digit format print
digit = "{number},{sname}".format (number = 98, sname = "Battery street")

#float
a_float = 3.14159
b_float = round(a_float,2)

#string format
str = "{str}".format (str = "Nervelabs Innovative")

#string concatenation
str1 = "Nervelabs "
str2 = "Innovative"
str3 = str1 + str2
print("Welcome to {}!".format(str3))



print(m, digit, b_float, sep ='\n')