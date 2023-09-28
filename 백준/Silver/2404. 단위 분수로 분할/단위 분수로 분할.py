from fractions import Fraction
import sys
input = sys.stdin.readline

p, q, a, n = map(int, input().split())
target = Fraction(p, q)

def backtrack(remaining, start, depth, product): # 남은 양, 단위분수 분모, 분수갯수, 단위분수 분모 곱
    # 남은 양이 0보다 작거나, 단위분수 분모 곱이 a보다 크거나, 분수갯수가 n보다 크면 return 0
    if remaining < 0 or product > a or depth > n: 
        return 0
    # 남은 양이 0이고, 분수 개수가 n보다 작거나 같으면 return 1
    if remaining == 0 and depth <= n: 
        return 1
    count = 0
    for i in range(start, int(a / product) + 1):
        unit_fraction = Fraction(1,i)
        if remaining-unit_fraction < 0 or product * i > a:
            continue
        # 1부터 a까지 돌면서 가능한 경우의 수만 count
        count += backtrack(remaining - unit_fraction, i, depth + 1, product * i) 
    return count

print(backtrack(target, 1, 0, 1))