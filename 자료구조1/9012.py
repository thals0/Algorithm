#  스택 자료구조를 이용한 풀이(처음 푼 방식)
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

# sum을 이용한 풀이 
a = int(input())

for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')