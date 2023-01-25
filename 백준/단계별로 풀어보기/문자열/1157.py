word = input().upper()
uni = list(set(word))
cnt=[]
for i in uni:
  count = word.count(i)
  cnt.append(count)
if cnt.count(max(cnt))>1:
  print("?")
else:
  max_index=cnt.index(max(cnt))
  print(uni[max_index])

# 이거 좀 어려웠다 꼭 다시 풀기 
