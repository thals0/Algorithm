import sys
sys.setrecursionlimit(10**7)

memo=[1,1]

def solution(n):
    if len(memo)-1>=n:
        return memo[n]
    else:
        memo.append(solution(n-1)+solution(n-2))

    return memo[n]%1234567