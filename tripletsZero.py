'''
Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.

Examples :

Input : arr[] = {0, -1, 2, -3, 1}
Output : (0 -1 1), (2 -3 1)

Explanation : The triplets with zero sum are
0 + -1 + 1 = 0 and 2 + -3 + 1 = 0  

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
Explanation : The triplets with zero sum is
1 + -2 + 1 = 0   
'''

'''
brute force way is to run 3 loops - i -> 0 to n-2, j -> i+1 to n-1 and k -> j+1 to n

more efficient way is to run 2 loops - i -> 0 to n-1, j -> i+1 to n and check if -(arr[i] + arr[j]) is present in the set. If yes, print/return the pair, else add the element to the set
'''


def findTriplets(arr): 
    n = len(arr)
    found = False
    for i in range(n - 1): 
    # set must be created after the first loop to avoid duplicate entries
        s = set() 
        for j in range(i + 1, n): 
            x = -(arr[i] + arr[j]) 
            if x in s: 
                print(x, arr[i], arr[j]) 
                found = True
            else: 
                s.add(arr[j])
        print(s) 
    if found == False: 
        print("No Triplet Found") 

if __name__ == "__main__":
  a = [0, -1, 2, -3, 1]
  findTriplets(a)
