import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

preorder = []
while True:
  key = input().split()
  if not key:
    break
  preorder.append(int(*key))

def getPost(preStart, preEnd):
  if preStart > preEnd:
    return

  root = preorder[preStart]

  if preStart == preEnd:
    return print(root)
  
  if preStart < preEnd:
    for i in range(preStart, preEnd+1):
      if preorder[i] > root:
        pos = i
        break
      else:
        pos = preEnd+1

  # print("position : ", pos)
  getPost(preStart+1, pos-1)
  getPost(pos, preEnd)
  print(root)

getPost(0, len(preorder)-1)