import itertools 

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def remove_non_primes(arr):
    return [num for num in arr if is_prime(num)]


def solution(numbers):
    arr = []
    for i in range(1, len(numbers)+1):
        arr.extend(list(itertools.permutations(numbers, i)))
    
    li = set()
    for i in arr:
        _str = ''.join(i)
        li.add(int(_str))
    
    li = remove_non_primes(li)
    
    return len(li)