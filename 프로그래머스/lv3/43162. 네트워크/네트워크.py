from collections import deque 
def bfs(i, n, computers, visited):
    q = deque()
    q.append(i)
    while q:
        x = q.popleft()
        for j in range(n):
            if computers[x][j] == 1 and j not in visited:
                visited.append(j)
                q.append(j)
                
def solution(n, computers):
    answer = 0
    visited = []
    for i in range(n):
        if i not in visited:
            bfs(i, n, computers, visited)
            answer += 1
    return answer