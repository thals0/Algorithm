import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
road = [0] * 100001

queue = deque()
queue.append(N)
road[N] = 1
while queue:
  x = queue.popleft()
  if x == K:
    print(road[x]-1)
    break
  for nx in (2*x, x-1, x+1):
    if 0 <= nx < 100001 and road[nx] == 0:
      if nx == 2*x:
        road[nx] = road[x]
        queue.appendleft(nx)
      else:
        road[nx] = road[x] + 1
        queue.append(nx)