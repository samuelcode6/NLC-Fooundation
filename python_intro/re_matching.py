#usr/bin/python3
"""string pattern matching
"""

# import a python standard library tool
# for performing  regex (regular expression)
import re

match = re.match('The [ \t]*(.*)python', 'The zen of python id The zen of python.')
print(match.groups())

match_bracket = re.match('[A-Za-z]*(.*)','')