from math import gcd

def solution(arr):
    stack = []
    for i in arr:
        if not stack:
            stack.append(i)
        else:
            a = stack.pop()
            stack.append(int(a*i/gcd(a, i)))
    return stack[0]