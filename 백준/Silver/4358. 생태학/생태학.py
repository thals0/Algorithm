import sys
input = sys.stdin.readline

trees = {}
while True:
  tree = input().rstrip()
  if not tree:
    break
  if tree in trees:
    trees[tree] += 1
  else:
    trees[tree] = 1

total = sum(trees.values())
trees = sorted(trees.items())

for key, val in trees:
  per = (val/total)*100
  print('%s %.4f' %(key, per))
