import sys
input = sys.stdin.readline

class Deque:
  def __init__(self):
    self.data = []
  def size(self):
    return len(self.data)
  def empty(self):
    if len(self.data) == 0:
      return 1
    else:
      return 0
  def push_front(self, x):
    self.data.insert(0, x)
  def push_back(self, x):
    self.data.append(x)
  def pop_front(self):
    if len(self.data) == 0:
      return -1
    else:
      ans = self.data[0]
      self.data = self.data[1:]
      return ans
  def pop_back(self):
    if len(self.data) == 0:
      return -1
    else:
      ans = self.data[-1]
      self.data = self.data[:-1]
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
deque = Deque()
for _ in range(n):
  cmd = input().split()
  op = cmd[0]
  if op == 'size':
    print(deque.size())
  elif op == 'empty':
    print(deque.empty())
  elif op == 'push_front':
    deque.push_front(cmd[1])
  elif op == 'push_back':
    deque.push_back(cmd[1])
  elif op == 'pop_front':
    print(deque.pop_front())
  elif op == 'pop_back':
    print(deque.pop_back())
  elif op == 'front':
    print(deque.front())
  elif op == 'back':
    print(deque.back())
  else:
    print('err')