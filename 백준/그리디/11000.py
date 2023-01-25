# import sys
# input = sys.stdin.readline

# n = int(input())
# cnt = 0 
# temp =[]
# for _ in range(n):
#   time = list(map(int, input().split()))
#   temp.append(time)

# # time[0] 기준으로 정렬 
# # temp = sorted(temp, key=lambda x: x[0])
# temp.sort(key=lambda x:x[0])

# S = []
# T = []

# for i in temp:
#   S.append(i[0])
#   T.append(i[1])

# for i in range(len(S)):
#   if i == 0:
#     cnt += 1
#   for j in range(i):
#     if T[j] <= S[i]:
#       cnt += 1

# print(cnt)

import sys
import heapq


heap = []
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort(key=lambda x: x[0])
heapq.heappush(heap, arr[0][1])  #첫번째 강의가 끝나는 시간을 넣음
for i in range(1, n):
    if heap[0] > arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])
print(len(heap))