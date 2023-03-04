t = int(input())
for _ in range(t):
  n,m = map(int, input().split())
  d = [[0]*30 for _ in range(30)]
  for i in range(30):
    d[i][i] = 1
    d[i][0] = 1
  for i in range(2, 30):
    for j in range(1, 30):
      d[i][j] = d[i-1][j-1] + d[i-1][j]
  
  print(d[m][n])