n = int(input())
num = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))