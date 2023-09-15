def solution(my_string):
    answer = 0
    for i in my_string:
        if 49 <= ord(i) < 65:
            answer += int(i)
    return answer