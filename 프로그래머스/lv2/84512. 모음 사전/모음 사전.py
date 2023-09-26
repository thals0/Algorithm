from itertools import product
def solution(word):
    ls = []
    
    for i in range(1, 6):
        for j in list(product('AEIOU', repeat=i)):
            ls.append(''.join(j))
    ls.sort()
    return ls.index(word) + 1
    