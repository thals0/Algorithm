n = int(input())

temp = []

for _ in range(n):
  op = int(input())
  temp.append(op)

temp.sort(reverse=True)

total = 0
for i in range(n):
  if(i%3 != 2):
    total += temp[i]
print(total)

# 이거는 왜 틀렸다고 나오지? 똑같은 의미 아닌가 
# for i in temp:
#   if(i%3 != 2):
#     total += i
# print(total)
