from collections import deque

def bfs(graph,v,visited):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = visited[n] + 1
                queue.append(i)
    return max(visited)

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    for g in graph:
        g.sort()
    visited = [0] * (n+1)
    m = bfs(graph,1,visited)

    return visited.count(m)