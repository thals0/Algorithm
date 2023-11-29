from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    q = deque()
    for city in cities:
        city = city.lower()
        if city not in q:
            if len(q) == cacheSize:
                q.popleft()
            q.append(city)
            answer += 5
        else:
            del q[q.index(city)]
            q.append(city)
            answer += 1
    return answer