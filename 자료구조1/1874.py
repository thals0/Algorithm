n = int(input())
stack=[]
op = []
cnt = 1
temp = 0
for i in range(n):
  num = int(input())
  while cnt <= num:
    stack.append(cnt)
    op.append('+')
    cnt+=1
  if stack[-1] == num:
    stack.pop()
    op.append('-')
  else:
    op.append('No')
    temp+=1
    break

if temp == 0:
  for i in op:
    print(i)
