n = int(input())
tips = []
for i in range(n):
  tips.append(int(input()))

sorted_tips = sorted(tips, reverse=True)

ans = []

for i in range(n):
  if sorted_tips[i]-i >= 0:
    ans.append(sorted_tips[i]-i)

print(sum(ans))