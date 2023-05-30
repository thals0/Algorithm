n = int(input())
arr = list(map(int, input().split()))
sub = []
arr = sorted(arr)
if n % 2 == 0:
  for i in range(n//2):
    sub.append(arr[i] + arr[-(i+1)])
else:
  arr_max = arr[-1]
  sub.append(arr_max)
  arr = arr[:n-1]
  for i in range(n//2):
    sub.append(arr[i] + arr[-(i+1)])

print(max(sub))