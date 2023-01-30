from collections import deque

def dfs(start):
  visited[start] = 1
  print(start, end=' ')
  for i in graph[start]:
    if visited[i] != 1:
      dfs(i)

def bfs(start):
  q = deque([start])
  visited[start] = 1
  while q:
    x = q.popleft()
    print(x, end=' ')
    for i in graph[x]:
      if visited[i] != 1:
        visited[i] = 1
        q.append(i)

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in graph:
  i.sort()

visited = [[] for _ in range(n+1)]
dfs(v)
print()

visited = [[] for _ in range(n+1)]
bfs(v)