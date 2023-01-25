# n,x=map(int,input().split())
# dic=[]
# for i in range(n):
#   dic.append(int(input()))
# for i in range(len(dic)):
#   if dic[i]<x:
#     print(dic[i], end=" ")

n,x=map(int,input().split())
dic =list(map(int, input().split()))
for i in range(n):
  if dic[i]<x:
    print(dic[i], end=" ")