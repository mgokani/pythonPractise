'''
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
'''

def islongPressed(name, typed):
  if len(name) > len(typed): return False
  d = {x:name.count(x) for x in set(name)}
  print(d)
  b = {y:typed.count(y) for y in set(typed)}
  print(b)
  c = list(d.values())
  print(c)
  a = list(b.values())
  print(a)
  if len(c) != len(a): return False
  i, j = 0, 0
  while (i < len(c) and j < len(a)):
    print(c[i], a[j])
    if c[i] > a[j]: return False
    else: 
      i+=1
      j+=1
      
  return True

if __name__ == "__main__":
  ret = islongPressed("alexee", "alxxee")
  print(ret)
