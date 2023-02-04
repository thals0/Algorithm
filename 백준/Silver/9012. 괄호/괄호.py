N = int(input())

for _ in range(N):
  ps = list(input())
  stack = []
  ans = ''
  for i in ps:
    if i == "(":
      stack.append(i)
    elif i == ")":
      if len(stack) == 0:
        # print("NO")
        ans = 'no'
        break
      else:
        stack.pop()
  if len(stack) == 0 and ans != 'no':
    print('YES')
  else:
    print('NO')

