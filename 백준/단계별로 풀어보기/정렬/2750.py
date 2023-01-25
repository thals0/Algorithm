a = int(input())
arr = []
for i in range(a):
  arr.append(int(input()))

arr = sorted(arr)
for i in range(len(arr)):
  print(arr[i])