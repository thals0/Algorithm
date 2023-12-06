def solution(s):
    answer = []
    # s to list 
    s = s[2:-2]
    s = s.split("},{")

    s.sort(key=lambda x: len(x))
    
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
        
    return answer