a=int(input())
for i in range(a):
  x,y=map(int, input().split())
  ans = x+y
  print("Case #%s: %s + %s = %s"%(i+1,x,y,ans))