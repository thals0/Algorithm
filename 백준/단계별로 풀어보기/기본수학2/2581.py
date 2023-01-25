a=int(input())
b=int(input())

sosu = []
for i in range(a,b+1):
  cnt = 0
  if i>1: # 여기를 자꾸 놓치네 
    for j in range(2,i):
      if i % j == 0:
        cnt += 1 
    if cnt == 0:
      sosu.append(i)

if len(sosu) > 0:
  print(sum(sosu))
  print(min(sosu))
else:
  print(-1)
