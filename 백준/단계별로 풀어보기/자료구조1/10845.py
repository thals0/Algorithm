import sys
input = sys.stdin.readline

class Queue:
  def __init__(self):
    self.data = []
  def size(self):
    return len(self.data)
  def empty(self):
    if len(self.data) == 0:
      return 1
    else:
      return 0
  def push(self, x):
    self.data.append(x)
  def pop(self):
    if len(self.data) == 0:
      return -1
    else:
      ans = self.data[0]
      self.data = self.data[1:]
      return ans
  def front(self):
    if len(self.data) == 0:
      return -1
    else:
      return self.data[0]
  def back(self):
    if len(self.data) == 0:
      return -1
    else:
      return self.data[-1]

n = int(input())
queue = Queue()
for _ in range(n):
  cmd = input().split()
  op = cmd[0]
  if op == 'size':
    print(queue.size())
  elif op == 'empty':
    print(queue.empty())
  elif op == 'push':
    queue.push(cmd[1])
  elif op == 'pop':
    print(queue.pop())
  elif op == 'front':
    print(queue.front())
  elif op == 'back':
    print(queue.back())
  else:
    print('err')