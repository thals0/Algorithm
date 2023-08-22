from collections import deque

def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    n = len(maps)
    m = len(maps[0])

    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
    if maps[n-1][m-1] == 1: 
        return -1
    return maps[n-1][m-1]