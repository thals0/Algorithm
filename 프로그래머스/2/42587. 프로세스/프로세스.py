from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for i,p in enumerate(priorities):
        q.append((p,i))
    _max = q[0][0]
    for i in range(len(q)):
        _max = max(q[i][0], _max)
    while q:
        p,idx = q.popleft()
        if p == _max:
            answer += 1
            if idx == location:
                return answer
            _max = -1
            for i in range(len(q)):
                _max = max(q[i][0], _max)
        else:
            q.append((p,idx))
    return answer