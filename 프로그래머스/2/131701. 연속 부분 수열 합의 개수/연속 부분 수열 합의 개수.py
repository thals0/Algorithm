from collections import deque
def solution(elements):
    q = deque(elements)
    arr = []
    n = len(elements)
    arr += elements
    for i in range(n-1):
        x = q.popleft()
        q.append(x)
        for j in range(n):
            elements[j] += q[j]
        arr += elements
    s = set(arr)
    return len(s)