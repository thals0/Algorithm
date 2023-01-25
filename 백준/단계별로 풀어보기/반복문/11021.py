# a=int(input())
# for i in range(a):
#   x,y=map(int, input().split())
#   print("Case #",i+1,":",x+y)

a=int(input())
for i in range(a):
  x,y=map(int, input().split())
  ans = x+y
  print("Case #%s: %s"%(i+1,ans))