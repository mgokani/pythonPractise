"""
In an array, find all triplets with sum 0
"""

class Solution(object):
  def tripletsZero(self, A):
    """
    :type A: list
    :rtype: list
    """
    l =  len(A)
    if l < 3: 
      print(None)
    for i in range(2, l):
      if A[i] + A[i-1] + A[i-2] == 0:
        print(A[i], A[i-1], A[i-2])

if __name__ == "__main__":
  A = [0, -2, 2]
  o = Solution()
  ret = o.tripletsZero(A)
