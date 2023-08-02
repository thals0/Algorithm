import math

def solution(progresses, speeds):
    answer = []
    cnt = 1
    q = [math.ceil((100-p) / s) for p, s in zip(progresses, speeds)]
    
    while q:
        v = q.pop(0)
        lst = q[:]
        for i in lst:
            if v >= i:
                q.pop(0)
                cnt += 1
            else:
                break
        answer.append(cnt)
        cnt = 1

    return answer