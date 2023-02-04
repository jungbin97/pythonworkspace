def dfs(graph, start, end, visited):
    # 현재노드 방문처리
    visited[start] = True
    result = 0
    for i in graph[start]:   # 해당 노드에 연결된 노드 모두 탐색
        if not visited[i]:
            dfs(graph, i, end, visited)

    if visited[end] == True:
        result = 1
        return result
    else:
        return result

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())    # 정점, 간선
    visited = [False] * (V+1)    # 노드 방문체크 리스트
    graph = [[] for _ in range(V+1)]    # [[] * V]

    for i in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)    # 노드 연결을 기록


    S, G = map(int, input().split())    # 검색할 노드(출발, 도착)


    print("#{} {}".format(test_case, dfs(graph, S, G, visited)))

