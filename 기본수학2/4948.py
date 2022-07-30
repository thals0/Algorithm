# 각 테스트 케이스마다 계속 소수를 계산하니까 시간 초과
while(1):
  a=int(input())
  if a ==0:
    break
  cnt=0
  for i in range(a+1,2*a+1):
    if i == 1:
      continue
    for j in range(2,int(i**0.5)+1):
      if i % j == 0:
        break
    else:
      cnt+=1
  print(cnt)

# 문제에서 주어진 범위 내에서 소수를 먼저 모두 구하고 시작
sosu =[]
for i in range(2,246913):
  cnt = 0 
  for j in range(2, int(i**0.5)+1):
    if i % j ==0:
      cnt += 1
      break
  if cnt == 0:
    sosu.append(i)
while(1):
  a = int(input())
  count = 0
  if a == 0:
    break
  for i in sosu:
    if a < i <= 2*a:
      count +=1
  print(count)
