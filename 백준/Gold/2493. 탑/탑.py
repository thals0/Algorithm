import sys
input = sys.stdin.readline

n = int(input())
cmd = list(map(int, input().split()))
ans = []
stack = []
for i in range(n):
  num = cmd[i]
  # stack이 비어있지 않으면 
  if stack:
    while stack:
      if stack[-1][0] < num:
        stack.pop()
        if not stack:
          print(0, end=' ')
      elif stack[-1][0] > num:
        print(stack[-1][1]+1, end=' ')
        break
      else:
        print(stack[-1][1]+1, end=' ')
        stack.pop()
        break
    stack.append([num, i])
  # stack이 비어있으면
  else:
    print(0, end=' ')
    stack.append([num, i])

