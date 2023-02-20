from itertools import combinations
import sys
input = sys.stdin.readline
s = input().rstrip()
l = []
stack = []
ans = set()

for idx, word in enumerate(list(s)):
  if word == '(':
    stack.append(idx)
  elif word == ')':
    start = stack.pop()
    end = idx
    l.append([start, end])

for i in range(1, len(l)+1):
  combi = combinations(l,i)
  for j in combi:
    tmp = list(s)
    for k in j:
      start, end = k
      tmp[start] = ''
      tmp[end] = ''
    ans.add(''.join(tmp))

for i in sorted(list(ans)):
  print(i)
