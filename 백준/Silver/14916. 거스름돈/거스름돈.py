n = int(input())
cnt = 0

while n:
  if n % 5 == 0:
    cnt += n // 5
    break
  n -= 2
  cnt += 1

if n < 0:
  print(-1)
else:
  print(cnt)