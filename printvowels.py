'''
Print vowels between consonants in a string
'''

import re

S = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
pattern = re.compile(r'(a|e|i|o|u|A|E|I|O|U){2,}')
a = (match.group() for match in pattern.finditer(S))
for i in a:
  print(i)
