from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
MAX_NUM = 100000
dist = [0] * (MAX_NUM+1)

def bfs():
  q = deque()
  q.append(n)
  dist[n] = 1
  while q:
    x = q.popleft()
    if x == k:
      print(dist[x]-1)
      break
    for nx in (x-1, x+1, 2*x):
      if 0 <= nx <= MAX_NUM and dist[nx]==0:
        if nx == 2*x:
          dist[nx] = dist[x]
          q.appendleft(nx)
        else:
          dist[nx] = dist[x] + 1
          q.append(nx)

bfs()