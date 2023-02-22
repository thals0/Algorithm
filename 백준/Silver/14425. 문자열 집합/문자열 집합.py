n,m = map(int, input().split())

ans = set(input() for _ in range(n))
cmd = [input() for _ in range(m)]
cnt = 0

for i in ans:
  cnt += cmd.count(i)

print(cnt)