n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))

# 시간복잡도 초과
# for i in arr:
#   print(arr2.index(i), end='')

dic = {arr2[i]: i for i in range(len(arr2))}
for i in arr:
  print(dic[i], end='')