'''
Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.
Examples :

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4
Explanation: Sum of elements between indices
2 and 4 is 20 + 3 + 10 = 33

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4
Explanation: Sum of elements between indices
1 and 4 is 4 + 0 + 0 + 3 = 7

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
Explanation: There is no subarray with 0 sum
'''

def findsubArray(a, s):
  n = len(a)
  minlen = n + 1
 
  for i in range(0, n):
    currSum = a[i]
    if currSum > s:
      return 1
    for j in range(i+1, n):
      currSum += a[j]
      print(currSum)
      if currSum > s and (j - i + 1) < minlen:
        minlen = (j - i + 1)
        print(minlen)
  return minlen

if __name__ == "__main__":
  a = [1, 4, 20, 3, 10, 5]
  s = 33
  print(findsubArray(a, s))
