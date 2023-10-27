from itertools import combinations

n, m = map(int, input().split())

nums = list(combinations(list(map(int, input().split())), 3))
arr = []
for i in nums:
    arr.append(sum(i))

arr.sort(reverse=True)
for i in arr:
    if i <= m:
        print(i)
        break