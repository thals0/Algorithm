import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# dfs 탐색
def dfs(x, w): # 시작 노드 번호, 현재 노드 가중치 
  # 반복문을 통해 현재 노드와 연결된 노드, 연결된 노드의 가중치 확인
  for a, b in graph[x]:
    # 탐색하지 않은 노드라면 탐색
    if visited[a] == -1:
      visited[a] = w + b # 이전 노드의 가중치와 현재 노드의 가중치 더함 
      dfs(a, w+b) # 재귀적으로 연결된 모든 노드 탐색 

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  p,c,w = map(int, input().split())
  graph[p].append([c,w])
  graph[c].append([p,w])

# print(graph)

visited = [-1] * (n+1) # 탐색 확인, 가중치 확인
visited[1] = 0 # 시작 노드는 가중치 0으로 초기화
dfs(1,0) # 첫 번째 노드를 dfs 탐색

# print(visited) # [-1, 0, 3, 2, 8, 13, 11, 9, 15, 28, 17, 17, 21]

# 위에서 찾은 노드에 대한 가장 먼 노드 찾기 
start = visited.index(max(visited))
visited = [-1] * (n+1)
visited[start] = 0
dfs(start, 0)

# print(visited) # [-1, 28, 31, 26, 36, 15, 35, 37, 43, 0, 19, 41, 45]
print(max(visited))