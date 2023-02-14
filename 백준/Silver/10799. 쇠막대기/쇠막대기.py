from collections import deque
cmd = deque(list(input()))
stack = []

cnt = 0
while cmd:
  a = cmd.popleft()
  if a == '(':
    if cmd[0] == ')':
      cmd.popleft()
      cnt += len(stack)
    else:
      stack.append('(')
  elif a == ')':
    stack.pop()
    cnt += 1

print(cnt)