from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    # for g in graph:
    #     g.sort()
        
    visited = [0] * (n+1)
    
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        n = q.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = visited[n] + 1
                q.append(i)
    
    m = max(visited)
    return visited.count(m)
