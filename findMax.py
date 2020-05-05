'''
Given a string of numbers, the task is to find the maximum value from the string, you can add a ‘+’ or ‘*’ sign between any two numbers.

Examples:

Input : 01231
Output : 
((((0 + 1) + 2) * 3) + 1) = 10
In above manner, we get the maximum value i.e. 10

Input : 891
Output :73
As 8*9*1 = 72 and 8*9+1 = 73.So, 73 is maximum.
'''

def findMax(s):
  n = len(s)
  res = int(s[0])
  for i in range(1, n):
    if s[i] == '0' or s[i] == '1' or res < 2:
      res += int(s[i])
    else:
      res *= int(s[i])
  return res



if __name__ == "__main__":
  s = '891'
  print(findMax(s))
