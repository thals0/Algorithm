def solution(citations):
    citations.sort()
    arr = []
    n = len(citations)
    for i in range(n):
        arr.append(min(n-i, citations[i]))
    return max(arr)