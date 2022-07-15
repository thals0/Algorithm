n=int(input())
for i in range(n):
  ls=list(input())
  count=0
  score=0
  ans=0
  for i in ls:
    if i == "O":
      score=1+count
      count+=1
    else:
      count=0
      score=0
    ans += score
  print(ans)