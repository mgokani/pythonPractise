"""
function to print pairs of numbers that sum up to n
for example: Given list of numbers 4, 1, 3, 5, 2, 6, 8, 7 - Print pairs of numbers whose sum equals 8
"""

def print_pairs(arr1, num):
    left = 0
    right = len(arr1)-1
    arr1 = sorted(arr1)
    while left < right:
        if arr1[left] + arr1[right] > num:
            right = right - 1
        elif arr1[left] + arr1[right] < num:
            left = left + 1
        elif arr1[left] + arr1[right] == num:
            return arr1[left],arr1[right]
        else:
            print ("Number pair not found")


if __name__  == "__main__":
    a = [4,1,3,5,2,6,8,6]
    number = 8
    print (print_pairs(a,8))
