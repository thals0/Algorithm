from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(start):
  cnt = 0
  q = deque([start])
  visited[start] = True
  while q:
    node = q.popleft()
    for i in graph[node]:
      if not visited[i]:
        visited[i] = True
        q.append(i)
        cnt += 1
  return cnt

visited = [False] * (1+n)

print(bfs(1))