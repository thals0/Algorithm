def solution(n):
    answer = 0
    arr = [i for i in str(n)]
    arr.sort(reverse=True)
    return int(''.join(arr))