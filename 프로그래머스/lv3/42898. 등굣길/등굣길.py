from collections import deque

def solution(m, n, puddles):
    answer = 0
    
    dx = [0, 1]
    dy = [1, 0]
    
    graph = [[0] * m for _ in range(n)]
    graph[0][0] = 1
    q = deque([])
    q.append((0,0))
    while q:
        x,y = q.popleft()
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <=nx < n and 0 <= ny <m:
                if [ny+1, nx+1] in puddles:
                    continue
                graph[nx][ny] += graph[x][y]
                if (nx, ny) not in q:
                    q.append((nx, ny))
        answer = graph[n-1][m-1] % 1000000007
    return answer 