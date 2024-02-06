from collections import deque
n,m = map(int,input().split())
board = []
for _ in range(n):
    tmp = input()
    arr = []
    for i in tmp:
        arr.append(i)
    board.append(arr)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[0]*m for _ in range(n)]

wq = deque()
q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 'D':
            xx, yy = i,j
        if board[i][j] == 'S':
            q.append((i,j,0))
            board[i][j] = '.'
            visited[i][j] = 1
        if board[i][j] == '*':
            wq.append((i,j))

wq1 = deque()
q1 = deque()

while q:
    while wq:
        wx,wy = wq.popleft()
        for i in range(4):
            wnx,wny = wx+dx[i], wy+dy[i]
            if wnx < 0 or wnx >= n or wny <0 or wny >= m:
                continue
            if board[wnx][wny] == '.':
                board[wnx][wny] = '*'
                wq1.append((wnx,wny))
    while q:
        x,y,cnt = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx <0 or nx>=n or ny <0 or ny>=m:
                continue
            if board[nx][ny] == '.' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q1.append((nx,ny,cnt+1))
            if board[nx][ny] == 'D':
                print(cnt+1)
                exit()
    
    wq = wq1
    wq1 = deque()
    q = q1
    q1 = deque()

print('KAKTUS')