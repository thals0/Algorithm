from heapq import *
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        if scoville[0] >= K:
            break
        if len(scoville) <= 1 and scoville[0] < K:
            return -1
        v1 = heappop(scoville)
        v2 = heappop(scoville)
        heappush(scoville, v1+(v2*2))
        answer += 1
    return answer