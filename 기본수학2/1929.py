# 시간 초과
a,b= map(int, input().split())
for i in range(a,b+1):
  cnt = 0
  if i > 1:
    for j in range(2,i):
      if i % j == 0:
        cnt += 1
    if cnt == 0:
      print(i)
