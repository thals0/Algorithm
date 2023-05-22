n = int(input())
dict = {}
for _ in range(n):
  str = input()
  b = str.split('.')[1]
  if b in dict:
    dict[b] += 1
  else:
    dict[b] = 1
sorted_dict = sorted(dict.items())
for item in sorted_dict:
  print(item[0], item[1])