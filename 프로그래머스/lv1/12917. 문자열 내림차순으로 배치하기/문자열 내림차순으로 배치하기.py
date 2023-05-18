def solution(s):
    arr = sorted(s, reverse = True)
    return ''.join(s for s in arr)