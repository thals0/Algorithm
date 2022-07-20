# a=int(input())
# for i in range(a+1):
#   while(i>1):
#     if a % i == 0:
#       print(i)
#       a = a/i
#     else:
#       break

a=int(input())
i=2
while a!=1:
  if a%i==0:
    print(i)
    a=a/i
  else: i+=1