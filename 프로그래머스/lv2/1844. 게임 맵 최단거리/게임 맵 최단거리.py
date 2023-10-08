from collections import deque

def solution(maps):   
    n = len(maps)
    m = len(maps[0])
    
    graph = [[0]*m for _ in range(n)]
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    q = deque()
    q.append((0,0))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or nx >=n or ny <0 or ny>=m:
                continue
            if maps[nx][ny] == 1 and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    
    if graph[n-1][m-1] == 0:
        return -1
    else: 
        return graph[n-1][m-1] + 1