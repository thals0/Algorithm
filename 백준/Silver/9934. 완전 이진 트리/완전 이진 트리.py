from collections import defaultdict

k = int(input())
inorder = list(map(int, input().split()))
tree = defaultdict(list)
i = 0

def getTree(i, inorder):
  n = len(inorder)
  if n > 1:
    root = inorder[n//2]
    tree[i].append(root)
    i += 1
    getTree(i, inorder[:n//2])
    getTree(i, inorder[n//2+1:])
  elif n == 1:
    tree[i].append(inorder[0])

getTree(i, inorder)

tree = list(tree.values())
for i in range(k):
  print(*tree[i])
