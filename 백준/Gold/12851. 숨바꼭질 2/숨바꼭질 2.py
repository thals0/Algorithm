from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)

visited = [0] * 100001

ans_count = 0
ans_way = 0

while q:
    x = q.popleft()
    if x == k:
        ans_count = visited[x]
        ans_way += 1
        continue

    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx < 100001:
            if visited[nx] == 0 or visited[nx] == visited[x] + 1:
                q.append(nx)
                visited[nx] = visited[x] + 1

print(ans_count)
print(ans_way)