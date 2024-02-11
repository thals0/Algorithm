def solution(seoul):
    answer = '김서방은 '
    for idx, s in enumerate(seoul):
        if s == "Kim":
            answer += str(idx)
    answer += "에 있다"
    return answer