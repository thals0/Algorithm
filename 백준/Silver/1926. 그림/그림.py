import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

arr = []
visited = [[0]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or nx >= n or ny<0 or ny >= m): continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            arr.append(bfs(i,j))

print(len(arr))
if len(arr) == 0:
    print(0)
else:
    print(max(arr))