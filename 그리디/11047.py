n, k = map(int, input().split())
cnt = 0
op = []
for _ in range(n):
  op.append(int(input()))
  
for i in op[::-1]:
  if k >= i:
    cnt += k//i
    k = k % i
  # if k == 0:
  #   break
print(cnt)