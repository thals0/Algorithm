def solution(numbers):
    nums = sorted(numbers, reverse=True)
    answer = nums[0]*nums[1]
    return answer