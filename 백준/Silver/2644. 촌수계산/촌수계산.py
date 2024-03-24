n = int(input())
i,j = map(int,input().split())
m = int(input())
board = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    board[a].append(b)
    board[b].append(a)

visited = [0] * (n+1)

def dfs(v, cnt):
    global answer
    if v == j:
        answer = cnt
        return
    for k in board[v]:
        if visited[k] != 1:
            visited[k] = 1
            dfs(k, cnt+1)

visited[i] = 1
dfs(i, 0)

if visited[j] == 1:
    print(answer)
else:
    print(-1)
