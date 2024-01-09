def dfs(start):
    visited[start] = 1
    node = 1
    for i in graph[start]:
        if visited[i] == 0:
            node += dfs(i)
    return node
            
def solution(n, wires):
    answer = -1
    global graph
    graph = [[] for _ in range(n+1)]
    global visited
    visited = [0]*(n+1)
    for w in wires:
        a,b = w
        graph[a].append(b)
        graph[b].append(a)
    ans_list = []
    for w in wires:
        a,b = w
        visited = [0]*(n+1)
        # 단선
        graph[a].remove(b)
        graph[b].remove(a)
        # 그룹1 노드 개수
        group1 = dfs(a)
        # 그룹2 노드 개수
        group2 = dfs(b)
        gap = abs(group1 - group2)
        ans_list.append(gap)
        
        # 선복구
        graph[a].append(b)
        graph[b].append(a)
    return min(ans_list)