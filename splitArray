'''
Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.
'''

def splitArray(arr):
  i = 0
  j = len(arr) - 1
  
  leftSum = arr[i]
  rightSum = arr[j]
  count = 0
  while i < j:
    if leftSum < rightSum:
      leftSum += arr[i+1]
      i += 1
      count += 1
      print(leftSum, i)
    elif leftSum > rightSum:
      rightSum += arr[j-1]
      j -= 1
      count += 1
      print(rightSum, j)
    elif leftSum == rightSum and count == len(arr) - 2:
      return i
    else: 
      return -1


if __name__ == "__main__":
  arr = [1,2,3,4,5,5]
  splitPoint = splitArray(arr)
  print(arr[0:splitPoint + 1])
  print(arr[splitPoint + 1:])
