# ----------------------------------------------------------------------------
# [baekjoon_1753] 최단경로
# ----------------------------------------------------------------------------
import heapq
import sys
input = sys.stdin.readline

INF = float('inf')

# 정점의 개수 V, 간선의 개수 E
v, e = map(int, input().split())

# 시작 노드 k
k = int(input())

graph = [[] for i in range(v+1)]

# 방문한적 있는지 체크
visited = [False] * (v+1)

distance = [INF] * (v+1)

# 모든 간선 입력받기
for _ in range(e):
    # u에서 v로 가는 간선 비용 w
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    # 시작노드로 가기 위한최단경로 0으로 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단거리 짧은 노드 부터 꺼내기
        dist, node = heapq.heappop(q)
        # 현재노드가 이미 처리된 노드면 무시(힙큐에 있는것보다 현재 노드가 작으면 이미 갱신된것)
        if distance[node] < dist:
            continue

        # 인접 노드 확인
        for i in graph[node]:
            cost = dist + i[1]
            # 현재노드를거쳐 다음노드를 이동하는거리가 더 짧으면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])