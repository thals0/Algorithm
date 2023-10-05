import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))


while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <0 or nx >= n or ny <0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] +1
            q.append((nx, ny))

ans = 0

for i in graph:
    if 0 in i:
        ans = 0
        break
    ans = max(ans, max(i))

print(ans-1)
