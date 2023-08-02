from collections import deque

def solution(numbers, target):
    arr = deque([0])
    for num in numbers:
        for _ in range(len(arr)):
            v = arr.popleft()
            arr.append(v - num)
            arr.append(v + num)
    return arr.count(target)