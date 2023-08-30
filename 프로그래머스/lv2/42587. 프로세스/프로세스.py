from collections import deque

def solution(priorities, location):
    answer = 0
    arr = []
        
    q = deque([])
    
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    
    while q:
        v = q.popleft()
        
        if len(q) == 0:
            arr.append(v)
            break
        
        li = sorted(q, key = lambda x : x[1], reverse=True)
        
        if v[1] >= li[0][1]:
            arr.append(v)
        else:
            q.append(v)
    
    for i in range(len(arr)):
        if arr[i][0] == location:
            answer = i+1
    return answer