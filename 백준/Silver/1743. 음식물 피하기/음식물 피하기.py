import sys
sys.setrecursionlimit(10000)

n,m,k = map(int, input().split())
trash = [[0]* (m+1) for _ in range(n+1)]
visited = [[0]* (m+1) for _ in range(n+1)]

for _ in range(k):
  r,c = map(int, input().split())
  trash[r][c] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
  visited[x][y]=1
  global cnt
  cnt += 1
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 1 <= nx < n+1 and 1 <= ny < m+1:
      if visited[nx][ny] == 0 and trash[nx][ny] == 1:
        dfs(nx, ny)

max_trash = 0
for i in range(1, n+1):
  for j in range(1,m+1):
    if trash[i][j] == 1 and visited[i][j] == 0:
      cnt = 0
      dfs(i,j)
      max_trash = max(max_trash, cnt)

print(max_trash)