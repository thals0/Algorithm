def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    answer_r = answer[::-1]
    answer += '0'
    answer += answer_r
    return answer