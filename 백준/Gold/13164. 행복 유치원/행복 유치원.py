n,k = map(int, input().split())
arr = list(map(int, input().split()))

sub = []

for i in range(len(arr)-1):
  sub.append(arr[i+1] - arr[i])

sub.sort(reverse=True)
print(sum(sub[k-1:]))