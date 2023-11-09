from heapq import *
def solution(operations):
    q = []
    heapify(q)
    for i in operations:
        op, n = i.split()
        if op == 'I':
            heappush(q, int(n))
        elif op == 'D' and len(q) != 0:
            if n == "-1":
                heappop(q)
            else:
                q.pop()
    if q:
        q.sort()
        return [q[-1], q[0]]
    else:
        return [0,0]