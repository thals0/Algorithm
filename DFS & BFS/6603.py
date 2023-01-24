# from itertools import combinations

# while True:
#   num = list(map(int, input().split()))
#   if len(num) == 1 and num[0] == 0:
#     break
#   items = num[1:]
#   ans = list(combinations(items, 6))
#   for i in ans:
#     for j in i:
#       print(j, end=' ')
#     print()
#   print()

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)
combi = [0 for i in range(13)]
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()