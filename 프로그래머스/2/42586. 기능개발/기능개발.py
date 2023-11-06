import math
def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        arr.append(math.ceil((100-progresses[i]) / speeds[i]))
    cnt = 0
    stack = []
    stack.append(arr[0])
    for i in arr:
        if i > stack[-1]:
            answer.append(cnt)
            cnt = 1
            stack.append(i)
        else:
            cnt += 1
    answer.append(cnt)
    return answer