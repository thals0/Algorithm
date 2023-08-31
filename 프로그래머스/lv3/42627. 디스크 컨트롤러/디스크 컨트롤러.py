from heapq import *

def solution(jobs):
    answer, i, total = 0,0,0
    l = len(jobs)
    h = []
    
    while i < l:
        for j in jobs:
            if 0 <= j[0] <= total:
                heappush(h, (j[1], j[0]))
                j[0] = -1
        if h:
            cur = heappop(h)
            total += cur[0]
            answer += total - cur[1]
            i += 1
        else:
            total += 1
    return answer//l
                