def solution(nums):
    answer = 0
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    n = len(nums)/2
    if len(dict) >= n:
        answer = n
    else:
        answer = len(dict)
    return answer