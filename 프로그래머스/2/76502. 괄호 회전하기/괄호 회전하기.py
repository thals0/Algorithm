from collections import deque
def solution(s):
    answer = 0
    
    def isRight(s):
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                # if i가 여는거면, stack.append
                if i == '(' or i == '[' or i == '{':
                    stack.append(i)
                else:
                    # if i가 닫는거면, stack.pop() 해서 모양비교 
                    # 모양 같으면 다음으로 넘어감, 모양 다르면 return False
                    last = stack.pop()
                    if last == '(' and i == ')':
                        continue
                    elif last == '[' and i == ']':
                        continue
                    elif last == '{' and i == '}':
                        continue
                    else:
                        return False

        if len(stack) != 0:
            return False
        else:
            return True
    
    q = deque()
    for i in s:
        q.append(i)
    
    for i in range(len(s)):
        start = q.popleft()
        q.append(start)
        if isRight(q):
            answer += 1
            
    return answer