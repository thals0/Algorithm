n=set(range(1,10001))
x=set()

for i in range(1,10001): #i=850
  for j in str(i):  # j = "8","5","0"
    i += int(j) #850+8+5+0
  x.add(i)

self_num= sorted(n-x)
for i in self_num:
  print(i)