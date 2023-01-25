# a,b,c=map(int,input().split());
# if b>=c:
#   print(-1)
# i=0
# while(True):
#   if a+b*i < c*i:
#     break;
#   i+=1
# print(i)

a,b,c=map(int,input().split());
if b>=c:
  print(-1)
else:
  print(a//(c-b)+1)