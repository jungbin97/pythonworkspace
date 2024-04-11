# ----------------------------------------------------------------------------
# [baekjoon_10282] 해킹
# ----------------------------------------------------------------------------
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
T = int(input())


def dijkstra(start):
    count = 0
    time = 0

    q = []
    distance = [INF] * (n+1)

    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    # 큐에 값이 존재한다면
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        # 인접노드 탐색
        for next_node, next_cost in graph[now]:
            cost = distance[now] + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    
    for i in range(1, n+1):
        if distance[i] != INF:
            count += 1
            time = max(time, distance[i])
    
    return count, time


for _ in range(T):
    # 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터 번호 c
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        # 양방향 간선
        graph[b].append((a, s))

    count, time = dijkstra(c)
    print(count, time)




# 요약
# 컴퓨터가 점진적으로 감염되기 시작한다.
# a, b가 의존성이 있다면 둘다 전파된다.
