# t= int(input())

# for i in range(t):
#   h,w,n = map(int,input().split())

# x=0
# while(1):
#   if n-h*x < 0:
#     break
#   y= n-h*x
#   x+=i
# print(y*100+x)

t=int(input())
for i in range(t):
  h,w,n = map(int,input().split())
  y=0
  x=0
  if n%h==0:
    y=h*100
    x=n//h
  else:
    y=(n%h)*100
    x=1+n//h
  print(y+x)

# 다시 + 내 코드 어디가 틀린지 확인
