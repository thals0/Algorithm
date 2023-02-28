import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  num = []
  for _ in range(n//10+1):
    num += list(map(int, input().split()))
  print(n//2+1)
  for i in range(1, len(num)+1, 2):
    print(sorted(num[:i])[i//2], end=' ')
  print()