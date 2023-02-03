class Stack:
  def __init__(self):
    self.data=[]
  def empty(self):
    if len(self.data) == 0:
      return 1
    else:
      return 0
  def size(self):
    return len(self.data)
  def push(self, X):
    self.data.append(X)
  def pop(self):
    if self.size() == 0:
      return -1
    else:
      return self.data.pop()
  def top(self):
    if self.size() == 0:
      return -1
    else:
      return self.data[-1]

import sys
input = sys.stdin.readline

num = int(input())
stack = Stack()
for _ in range(num):
  cmd = input().split()

  op = cmd[0]
  if op == 'push':
    stack.push(cmd[1])
  elif op == 'empty':
    print(stack.empty())
  elif op == 'pop':
    print(stack.pop())
  elif op == 'size':
    print(stack.size())
  elif op == 'top':
    print(stack.top())
  else:
    print('err')