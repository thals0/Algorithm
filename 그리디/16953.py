a, b = map(int, input().split())
cnt = 0

while True:
  if a >= b:
    break
  if b%2 != 0 and b%10 != 1:
    print(-1)
    break
  if b%10 == 1:
    b//=10
    cnt +=1 
  else:
    b/=2
    cnt += 1

if a == b:
  print(cnt + 1)
elif a > b:
  print(-1)