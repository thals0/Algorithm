n,k = map(int, input().split())
ans= []
arr = [i for i in range(1,n+1)] 
front = 0
for i in range(n):
  front += (k-1)
  if front >= len(arr):
    front %= len(arr)
  ans.append(str(arr[front]))
  arr.pop(front)

print("<",', '.join(ans),">", sep="")