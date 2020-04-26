'''print top k most frequent words in a string/file'''
from collections import OrderedDict 


inp = '''Welcome to the world of Geeks This portal has been created to provide well written well thought and well explained solutions for selected questions If you like Geeks for Geeks and would like to contribute here is your chance You can write article and mail your article to contribute at geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help thousands of other Geeks'''


d = {}
k = 5
for word in inp.split(' '):
  try:
    d[word] += 1
  except KeyError:
    d[word] = 1

# sort a dict based on values
c = OrderedDict(sorted(d.items(), key = lambda t:t[1], reverse = True))

count = 0
for key, value in c.items():
  print(key, value)
  count += 1
  if count == k:
    break
