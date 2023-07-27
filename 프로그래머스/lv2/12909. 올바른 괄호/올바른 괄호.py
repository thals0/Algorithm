def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and len(stack) != 0:
            stack.pop()
        else:
            return False
    if len(stack) > 0:
        return False
    return True