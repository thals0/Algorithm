import heapq
import sys
input = sys.stdin.readline

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)

c = 0
s = 0

while len(card) > 1:
  n1 = heapq.heappop(card)
  n2 = heapq.heappop(card)
  c = n1 + n2
  s += c
  heapq.heappush(card, c)

print(s)
