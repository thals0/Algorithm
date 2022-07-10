dic=[]
for i in range(9):
  dic.append(int(input()))

x = max(dic)
print(x)
print(dic.index(x)+1)