def solution(n, lost, reserve):
    lst = sorted(lost)
    reserve.sort()
    for i in lst:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    lst2 = sorted(lost)
    for i in lst2:
        if i-1 in reserve:
            reserve.remove(i-1)
            lost.remove(i)
        elif i+1 in reserve:
            reserve.remove(i+1)
            lost.remove(i)
    return n-len(lost)