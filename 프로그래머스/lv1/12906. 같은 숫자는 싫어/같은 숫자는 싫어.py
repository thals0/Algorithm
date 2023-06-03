def solution(arr):
    stack = []
    stack.append(arr[0])
    for i in range(1, len(arr)):
        if stack[-1] == arr[i]:
            continue
        stack.append(arr[i])
    return stack