def solution(sizes):
    max_w, max_h = 0,0
    for i in sizes:
        i.sort()
    for i in sizes:
        if max_w < i[0]:
            max_w = i[0]
        if max_h < i[1]:
            max_h = i[1]
    return max_w * max_h