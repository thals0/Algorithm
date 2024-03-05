from collections import defaultdict
def solution(nums):
    answer = 0
    dict = defaultdict(int)
    for num in nums:
        dict[num] += 1
    
    if len(nums)/2 > len(dict):
        answer = len(dict)
    else:
        answer = len(nums)/2
    return answer