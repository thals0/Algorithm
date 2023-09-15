from collections import deque
def solution(number, k):
    q = deque()
    stack = deque()

    for n in number:
        q.append(n)

    while q and k:
        while stack and stack[-1] < q[0]:
            stack.pop()
            k -= 1
            if not k:
                break
        stack.append(q.popleft())

    while k and stack:
        stack.pop()
        k -= 1

    return "".join(stack + q)