from collections import deque
def solution(progresses, speeds):
    answer = []
    cnt = 1
    q = deque()
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            q.append((100-progresses[i]) // speeds[i])
        else:
            q.append((100-progresses[i]) // speeds[i] + 1)
    while q:
        v = q.popleft()
        lst = list(q)
        for i in lst:
            if v >= i:
                q.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)
        cnt = 1
    return answer