n = int(input())
dp = [[0] * 10 for _ in range(n)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(1, 10):
        t = 0
        for k in range(j - 2, j + 3):
            if 0 < k < 10:
                t += dp[i - 1][k]
                t %= 987654321
        dp[i][j] = t

ans = 0
for i in range(10):
    ans += dp[n - 1][i]
    ans %= 987654321

print(ans)
