# 메모리 초과
import sys

# n = int(input())
# m = []
# for i in range(n):
#   m.append(int(sys.stdin.readline()))
# m.sort()
# for i in m:
#   print(i)

n = int(sys.stdin.readline())
m = [0] * 10001

for i in range(n):
  m[int(sys.stdin.readline())] += 1

for i in range(10001):
  if m[i] != 0:
    for j in range(m[i]):
      print(i)

