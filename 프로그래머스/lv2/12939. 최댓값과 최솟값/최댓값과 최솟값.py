def solution(s):
    answer = []
    arr = list(map(int, s.split(' ')))
    arr.sort()
    answer.append(str(arr[0]))
    answer.append(str(arr[len(arr)-1]))
    return " ".join(answer)