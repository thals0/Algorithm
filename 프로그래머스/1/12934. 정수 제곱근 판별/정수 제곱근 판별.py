from math import *
def solution(n):
    answer = 0
    tmp = sqrt(n)
    if tmp % 1 == 0:
        answer = (tmp+1)**2
    else:
        answer = -1
    return answer