#!/usr/bin/python3
"""
Most important python core data types
"""
# Number Type
integer = 12345
float = 1234.5
complex_num = 123+3j
binary = 0b101

print('this is an integer', integer, type(integer), sep=',')
print('this is a float', float, type(float), sep=',')
print('this is a complex number', complex_num, type(complex_num), sep=',')
print('this is sbinary representation of an integer', binary, type(binary), sep=',')


#String type
single_quoted = 'This is a single quoted string'
double_quoted = 'This is a double quoted string'
raw_string = r'This is a raw string'


#Formatted strings
name = input('enter your name: ')
formatted_string = f'Good Evening, {name}'
formatted_string2 = 'Good Evening, {}'.format(name)
formatted_string3 ='Good Evening, %s' %name

print(single_quoted, double_quoted, raw_string, formatted_string, formatted_string2, formatted_string3, sep='\n')
