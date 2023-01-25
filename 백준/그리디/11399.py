n = int(input())
cmd = list(map(int, input().split()))

cmd.sort()
ans = 0
temp = []
for i in cmd:
  ans += i
  temp.append(ans)

print(sum(temp))