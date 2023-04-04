n, m = map(int, input().split())
bulb = [0] + list(map(int, input().split()))
for _ in range(m):
  a,b,c = map(int, input().split())
  if a == 1:
    bulb[b] = c
  elif a == 2:
    for i in range(b, c+1):
      if bulb[i] == 0:
        bulb[i] = 1
      else:
        bulb[i] = 0
  elif a == 3:
    for i in range(b, c+1):
      if bulb[i] == 1:
        bulb[i] = 0
  elif a==4:
    for i in range(b, c+1):
      if bulb[i] ==0:
        bulb[i] = 1

print(*bulb[1:])