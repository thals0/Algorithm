from collections import deque

n = int(input())
graph = []
cnt = 0
for _ in range(n):
  m = list(map(int, input()))
  graph.append(m)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  val = 1
  q = deque()
  q.append((x,y))
  graph[x][y] = 0
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >=n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        val += 1
        q.append((nx,ny))
  return val

ans = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      ans.append(bfs(i,j))
      cnt += 1
ans.sort()
print(cnt)
for i in ans:
  print(i)
