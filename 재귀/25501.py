def recursion(s, l, r):
    if(l >= r):
      return 1
    elif(s[l] != s[r]): 
      return 0
    else: 
      return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

print("ABBA: %d\n", isPalindrome("ABBA")) # 1
print("ABC: %d\n", isPalindrome("ABC")) # 0

n = int(input())


