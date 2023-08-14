def solution(k, tangerine):
    cnt = 0
    dic = {}
    for i in tangerine:
        if i not in dic :
            dic[i] = 1
        else:
            dic[i] += 1
            
    sorted_val = sorted(list(dic.values()), reverse=True)
    val = 0
    
    for i in sorted_val:
        val += i
        cnt += 1
        if val >= k: break
    return cnt