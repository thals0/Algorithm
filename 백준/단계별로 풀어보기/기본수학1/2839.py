n=int(input())
bag=0
while n >=0:
  if n%5==0:
# 어차피 5로 나눈 나머지가 0이니까 n/5를 bag에 더하는걸 했는데
# 왜 n//5가 아니면 계산이 안되지?
# 4.0 이렇게 분수 형태로 나와서 안되는 구나,, 대박 
    bag+= (n/5)
    print(bag)
    break
  n -=3
  bag +=1
else: 
  print(-1)