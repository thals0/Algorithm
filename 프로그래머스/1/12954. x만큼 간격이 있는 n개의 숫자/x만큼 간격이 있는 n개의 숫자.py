def solution(x, n):
    answer = []
    tmp = 0
    for i in range(n):
        tmp += x
        answer.append(tmp)
    return answer