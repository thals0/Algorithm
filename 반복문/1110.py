# a를 문자열로 
a=input()
if len(a)<2:
  x = a+"0"
else:
  x = a
i = 0
while True:
  y=x[0]+x[1]
  if len(y)==1:
    y=y[0]
  else:
    y=y[1]
  x = x[1]+y[0]
  i +=1
  if a==x:
    break
print(i)

# a를 int로
a=int(input())
ans = a
i = 0

if a//10 == 0:
  x = a * 10
else:
  x = a 

while True:
  y= x//10 + x%10
  x = (x%10)*10 + y%10
  i += 1
  if ans==x:
    break
print(i)
