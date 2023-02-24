import sys, heapq

input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
	num_list = list(map(int, input().split()))
	if not q: 
		for num in num_list:
			heapq.heappush(q, num) 
	else:
		for num in num_list: 
			if q[0] < num:
				heapq.heappop(q)
				heapq.heappush(q, num)
print(q[0])