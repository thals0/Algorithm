from collections import deque
def solution(priorities, location):
    q = deque()
    answer = 0
    for i, val in enumerate(priorities):
        q.append((i, val))
    while q:
        m = q[0][1]
        for i in q:
            if m < i[1]:
                m = i[1]
        cur = q.popleft()
        if m > cur[1]:
            q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
        
            