from collections import deque
t = int(input())

for _ in range(t):
    dx = [1,2,2,1,-1,-2,-2,-1]
    dy = [2,1,-1,-2,-2,-1,1,2]

    l = int(input())
    now_x, now_y = map(int,input().split())
    xx, yy = map(int,input().split())

    visited = [[0]*l for _ in range(l)]

    q = deque()
    q.append((now_x, now_y, 0))
    visited[now_x][now_y] = 1
    while q:
        x,y,cnt = q.popleft()
        if x == xx and y == yy:
            print(cnt)
            break
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= l or ny <0 or ny >= l:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny,cnt+1))