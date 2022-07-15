a=int(input())
b=int(input())
c=int(input())
x = a * b * c
x= list(str(x))
for i in range(10):
  print(x.count(str(i)))