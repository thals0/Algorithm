import sys
input = sys.stdin.readline

num = int(input())

# stack 자료 구조를 이용하여 구현 
# 이 코드 왜 '출력방식이 잘 못 되었습니다'라고 뜨지?
for _ in range(num):
  cmd = input()
  cmd += " "
  stack = []
  for i in cmd:
    if i!=" ":
      stack.append(i)
    else:
      while stack:
        print(stack.pop(), end='')
      print(' ', end='')


# stack 자료 구조를 이용하여 구현 
# 정답 코드
N=int(input())

for i in range(N):
  string=input()
  string+=" "
  stack=[]
  for j in string:
    if j!=" ":
      stack.append(j)
    else:
      while stack:
        print(stack.pop(), end='')
      print(' ', end='')


# list 내부 기능으로 구현 
for _ in range(num):
  cmd = input().split()
  for j in cmd:
    print(j[::-1], end=' ')