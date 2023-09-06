def solution(t, p):
    answer = 0
    arr = []
    for i in range(len(t)-len(p)+1):
        arr.append(t[i:len(p)+i])
    for i in arr:
        if i <= p:
            answer +=1 
    return answer