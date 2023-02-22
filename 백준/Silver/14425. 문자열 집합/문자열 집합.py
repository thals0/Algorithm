n,m = map(int, input().split())
ans = set()
cmd = []
cnt = 0

for _ in range(n):
  ans.add(input())

for _ in range(m):
  cmd.append(input())

for i in ans:
  cnt += cmd.count(i)

print(cnt)