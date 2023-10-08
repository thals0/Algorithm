def solution(numbers, target):
    def dfs(num, i, s):
        nonlocal cnt
        s += num
        if i == len(numbers):
            if s == target:
                cnt += 1
            return 
        dfs(+numbers[i], i+1, s)
        dfs(-numbers[i], i+1, s)
    cnt = 0 
    dfs(0, 0, 0)
    return cnt