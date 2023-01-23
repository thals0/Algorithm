from itertools import combinations

while True:
  num = list(map(int, input().split()))
  if len(num) == 1 and num[0] == 0:
    break
  items = num[1:]
  ans = list(combinations(items, 6))
  for i in ans:
    for j in i:
      print(j, end=' ')
    print()
  print()
