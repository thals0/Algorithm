cnt = 0
while True:
  L, P, V = map(int, input().split())
  if L == 0 and P == 0 and V == 0:
    break
  # min((V%P), L) 주의 
  ans = (V//P)*L + min((V%P), L)
  cnt += 1
  print("Case %d: %d" %(cnt, ans))