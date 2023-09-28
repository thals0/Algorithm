def solution(clothes):
    ans = 1
    dict = {}
    for i in clothes:
        if i[1] not in dict:
            dict[i[1]] = 0
        dict[i[1]]+=1
        
    for i in dict.values():
        ans=(i+1)*ans
    return ans-1