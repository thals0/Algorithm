n,m = map(int, input().split())

listen = []
see = []

for _ in range(n):
  listen.append(input())

for _ in range(m):
  see.append(input())

listenSee = sorted(list(set(listen).intersection(see)))

print(len(listenSee))
for i in listenSee:
  print(i)