h,m =input().split()
h=int(h)
m=int(m)
making=int(input())
if m + making < 60:
  print(h,m+making)
elif h+((m + making)//60) < 24 and m + making >= 60:
  print(h+(m + making)//60,(m + making)%60)
elif h+((m + making)//60) >=24 and m + making >= 60:
  print((h+((m + making)//60))-24,(m + making)%60)
