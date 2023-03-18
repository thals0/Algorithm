import sys
input = sys.stdin.readline

n = int(input())
dp = [[0,0] for _ in range(n+1)]
# print(dp)
arr = [0]

for i in range(1,n+1):
  dp[i][1] = 1e9

for i in range(n-1):
  arr.append(list(map(int, input().split())))
k = int(input())

# print(arr)

for i in range(2, n+1):
  dp[i][0] = dp[i-1][0] + arr[i-1][0]
  if i>2 :
    dp[i][0] = min(dp[i][0], dp[i-2][0] + arr[i-2][1])
  if i>3:
    dp[i][1] = min(dp[i-1][1]+arr[i-1][0], dp[i-2][1]+ arr[i-2][1], dp[i-3][0]+k)

# print(dp) # [[0, 0], [0, 0], [1, 0], [2, 0], [4, 3], [7, 5]]
print(min(dp[n][0], dp[n][1])) # 5