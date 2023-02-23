import sys
import heapq
input = sys.stdin.readline


test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [False] * 1_000_001

    n = int(input())

    for key in range(n):
        cmd = input().split()
        if cmd[0] == 'I':
            heapq.heappush(min_heap, (int(cmd[1]), key))
            heapq.heappush(max_heap, (int(cmd[1]) * -1, key))
            visit[key] = True 

        elif cmd[0] == 'D':
            if cmd[1] == '-1': 
                while min_heap and not visit[min_heap[0][1]]: 
                    heapq.heappop(min_heap) 
                if min_heap:
                    visit[min_heap[0][1]] = False 
                    heapq.heappop(min_heap)
            elif cmd[1] == '1':
                while max_heap and not visit[max_heap[0][1]]: 
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')