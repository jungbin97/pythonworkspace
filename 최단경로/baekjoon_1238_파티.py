# ----------------------------------------------------------------------------
# [baekjoon_1238] 파티
# ----------------------------------------------------------------------------
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

# n명의 학생 마을, m개의 단방향 간선, 파티 할 X번 마을 
n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    # a 시작 노드, b도착노드 c 비용
    a, b, c = map(int, input().split())
    # 단방향 이동
    graph[a].append((b, c))

def dijkstra(start, end):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐에 값이 존재하면
    while q:
        dist, now = heapq.heappop(q)
        # 최단거리 테이블 이미 최단거리 값이면 무시
        if distance[now] < dist:
            continue
        
        # 해당 노드의 인접노드 탐색
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost: 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]

result = 0

for i in range(1, n+1):
    start_end = dijkstra(i, x)
    end_start = dijkstra(x, i)
    
    result = max(result, start_end + end_start)


print(result)


# 요약
# N개의 마을, N명의 학생이 X번 마을에 모여 파티함.
# 학생들은 최단 거리로 이동함.(단방향으로 이동가능)
# 오고 가는데 가장 많은 시간을 소비하는 학생을 구하라.