"""
function to count how many times a substring appears in the larger String.
"""

def find_count(str1, str2):
    counter = 0
    for i in range(len(str1)):
        if str1[i:(i+len(str2))] == str2:
            counter+=1
    return counter

if __name__  == "__main__":
    a = "anbanbanbanb"
    b = input("Enter substring:")
    if b is '':
        print ("Enter a valid substring")
    else:
        print ("Number of times %s is found in %s is %d" %(b,a,find_count(a,b)))
