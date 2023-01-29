from collections import deque

n = int(input())
graph = []
maxNum = 0

for _ in range(n):
  a = list(map(int, input().split()))
  graph.append(a)
  for j in a:
    if j > maxNum:
      maxNum = j

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y, num):
  q = deque()
  q.append((x,y))
  visited[x][y] = 1
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      if graph[nx][ny] > num and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        q.append((nx,ny))

ans = []

for num in range(maxNum):
  cnt = 0
  visited = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if graph[i][j] > num and visited[i][j] == 0:
        bfs(i,j,num)
        cnt += 1
  ans.append(cnt)

print(max(ans))