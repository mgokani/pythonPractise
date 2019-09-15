'''
Write a Python program to remove the parenthesis area in a string. Go to the editor
Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
Expected Output:
example
w3resource
github
stackoverflow
'''

import re

data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

pattern = re.compile(r'([a-z0-9]+)(\s\(\.com\))?')
for i in data:
  new_data = pattern.sub(r'\1', i)
  print(new_data)
