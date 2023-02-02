from collections import deque
n = int(input())
dist = [0]*(10**6+1)

def bfs():
  q = deque()
  q.append(1)
  while q:
    x = q.popleft()
    if x == n:
      print(dist[x])
      break
    for nx in (3*x, 2*x, x+1):
      if 0<= nx <= 10**6 and dist[nx] == 0:
        dist[nx] = dist[x] + 1
        q.append(nx)

bfs()