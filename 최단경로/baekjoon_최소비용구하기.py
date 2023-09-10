# ----------------------------------------------------------------------------
# [baekjoon_1916] 최소 비용 구하기
# ----------------------------------------------------------------------------
import sys
import heapq
input = sys.stdin.readline

INF = float('inf')

# N 도시 개수
N = int(input())
# 버스 개수
M = int(input())

graph = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(M):
    # 출발 도시 번호, 도착지 도시 번호, 버스 비용
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start_city, end_city = map(int, input().split())


distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    # 우선순위 큐에 삽입 튜플 순서(거리, 노드번호)
    heapq.heappush(q, (0, start))
    distance[start]= 0

    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue

        # 인접 노드 체크
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start_city)

print(distance[end_city])

