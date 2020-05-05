'''
Given two unsorted arrays of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.

Examples:

Input :  arr1[] = {-1, -2, 4, -6, 5, 7}
         arr2[] = {6, 3, 4, 0}  
         x = 8
Output : 4 4
         5 3

Input : arr1[] = {1, 2, 4, 5, 7} 
        arr2[] = {5, 6, 3, 4, 8}  
        x = 9
Output : 1 8
         4 5
         5 4
'''

def findPairs(a1, a2, x):
  n = len(a1)
  m = len(a2)
  s = set()
  found = False
  for i in range(0, n):
    s.add(x-a1[i])
  for j in range(0, m):
    if a2[j] in s:
      print(x-a2[j], a2[j])
      found = True
  if found == False:
    print('no pairs found')


if __name__ == "__main__":
  a1 = [1, 2, 4, 5, 7]
  a2 = [5, 6, 3, 4, 8]
  x = 9
  findPairs(a1, a2, x)
