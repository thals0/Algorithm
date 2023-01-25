# n=int(input())
# arr=list(map(int,input().split()))
# m = max(arr)
# x=0
# for i in range(n):
#   x += arr[i]/m*100

# print(x/n)

# n=int(input())
arr=list(map(int,input().split()))
m = max(arr)
x=0
for i in range(len(arr)):
  x += arr[i]/m*100

print(x/len(arr))