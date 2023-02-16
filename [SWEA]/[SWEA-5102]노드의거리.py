# 가중치 없는 그래프에서(간선의 가중치가 1인) 최단거리 찾기 => BFS로 구현
# from collections import deque

# def bfs(S, G):
#     queue.append(S)     # 큐에 시작점 추가
#     visited[S] = True   # 방문처리

#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:  # 인접노드 체크
#             if not visited[i]:
#                 visited[i] = True # 방문처리
#                 distance[i] = distance[v] + 1
#                 queue.append(i)
#                 if i == G:  # 도착노드
#                     return distance[i]

# for test_case in range(1, int(input())+1):
#     V, E = map(int, input().split())    # V:노드 개수 E:간선 개수
#     graph = [[] for _ in range(V+1)]      # 그래프를 저장할 2차원 리스트
#     visited = [False] * (V + 1)     
#     distance = [0] * (V + 1)
#     queue = deque()
    
#     # 그래프 설정(양방향 그래프)
#     for i in range(E드드:
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
#     # S: 출발노드 G: 도착노드
#     S,G = map(int, input().split())

#     print("#{} {}".format(test_case, bfs(S, G))
# --------------------------------------------------------------
#   testcase 10개 중 9개 통과 무엇을 놓쳤을까???
#   => 출발노드와 도착노드가 연결되어있지 않을 경우 고려하지 않음
# --------------------------------------------------------------
# --------------------------------------------------------------
from collections import deque

def bfs(S, G):
    queue.append(S)     # 큐에 시작점 추가
    visited[S] = True   # 방문처리

    while queue:
        v = queue.popleft()
        for i in graph[v]:  # 인접노드 체크
            if not visited[i]:
                visited[i] = True # 방문처리
                distance[i] = distance[v] + 1
                queue.append(i)
                if i == G:  # 도착노드
                    return distance[i]
    return 0
for test_case in range(1, int(input())+1):
    V, E = map(int, input().split())    # V:노드 개수 E:간선 개수
    graph = [[] for _ in range(V+1)]      # 그래프를 저장할 2차원 리스트
    visited = [False] * (V + 1)     
    distance = [0] * (V + 1)
    queue = deque()
    
    # 그래프 설정(양방향 그래프)
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # S: 출발노드 G: 도착노드
    S,G = map(int, input().split())

    print("#{} {}".format(test_case, bfs(S, G)))
# --------------------------------------------------------------
# ------ distance 리스트 없이 노드를 기록할 수 없을까? ------------