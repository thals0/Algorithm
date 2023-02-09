n = int(input())

cmd = list(input())
num=[int(input()) for _ in range(n)]

stack = []
for i in cmd:
  if i.isalpha():
    stack.append(num[ord(i)-65])
  else:
    str2 = stack.pop()
    str1 = stack.pop()
    if i =='+' :
      stack.append(str1+str2)
    elif i == '-' :
      stack.append(str1-str2)
    elif i == '*' :
      stack.append(str1*str2)
    elif i == '/' :
      stack.append(str1/str2)

print('%.2f' %stack[0])




