from itertools import permutations

def solution(numbers):
    def isSosu(n):
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    s = set()
    for i in range(1, len(numbers)+1):
        for j in list(permutations(numbers,i)):
            s.add(int(''.join(j)))
    answer = 0
    for i in s:
        if isSosu(i) and i != 0 and i != 1:
            answer += 1
    
    return answer