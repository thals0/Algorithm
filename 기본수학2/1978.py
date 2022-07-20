n = int(input())
numbers = map(int, input().split())

x = 0 # 소수
for num in numbers:
  cnt = 0 # 1과 자신 제외한 약수 cnt
  if num > 1:
    for i in range(2,num):
      if num % i ==0:
        cnt +=1
    if cnt == 0:
      x += 1
print(x)