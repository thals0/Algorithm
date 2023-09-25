import math
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        s = int(math.sqrt(i))
        if s*s == i:
            answer -= i
        else: answer += i
    return answer