def solution(s):
    arr = s.split(" ")
    l = []
    for i in arr:
        if i != "":
            l.append(i[0].upper() + i[1:].lower())
        else:
            l.append(i)
    return ' '.join(l)