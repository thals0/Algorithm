# a,b,v=map(int,input().split())
# day=1
# sum=0
# while(sum<v):
#   sum+=a
#   if sum>=v:
#     break
#   sum-=b
#   day+=1
# print(day)

a,b,v=map(int,input().split())
day=(v-b)//(a-b)
if (v-b)%(a-b) ==0:
  print(day)
else:
  print(day+1)
