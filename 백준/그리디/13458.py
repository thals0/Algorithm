n = int(input())
a = map(int, input().split())
b, c = map(int, input().split())
cnt = 0 

for i in a:
  i = i - b
  cnt += 1
  if i > 0 and i % c != 0 :
    cnt += (i // c) + 1
  elif i > 0 and i%c == 0:
    cnt += i // c

print(cnt)