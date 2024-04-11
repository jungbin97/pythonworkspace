# ----------------------------------------------------------------------------
# [baekjoon_1504] 특정한 최단 경로
# ----------------------------------------------------------------------------
import sys
import heapq
input = sys.stdin.readline

INF = 1e9
# 정점 개수N, 간선의 개수 E
n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 간선 초기화(양방향)
for _ in range(e):
    # a 노드에서 b노드 양방향, 간선이 비용은 c라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = 1, n
node1, node2 = map(int, input().split())

# 다익스트라
def dijkstra(start, end):
    q = []
    # 최단 거리 테이블 초기화
    distance = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 비어있지 않다면
    while q:
        dist, now = heapq.heappop(q)
        # 이미 최단거리 테이블이 더 적은경우 최단거리이므로 무시한다.
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[end]



value1 = dijkstra(start, node1) + dijkstra(node1, node2) + dijkstra(node2, end)
value2 = dijkstra(start, node2) + dijkstra(node2, node1) + dijkstra(node1, end)

if value1 >= INF and value2 >= INF:
    print(-1)
else:
    print(min(value1, value2))


# 요약
# 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고한다.(양방향 이동가능)
# 임의로 주어진 두정점은 반드시 통과해야한다.

# 두정점을 지나는 최단 경로가 없을 경우 -1 출력
# 최단거리면서 두정점을 지나는 최단거리를 출력하라.



# 풀이
# 반드 방문해야하는 노드는 어떻게?

# 다익스트라 경로를 쪼개자.
# 1) 1번
# start => node1  =====>> dijkstra(start, node1)
# node1 => node2  =====>> dijkstra(node1, node2)
# node2 => end    =====>> dijkstra(node2, end)

# 2) 2번
# start => node2
# node2 => node1
# node1 => end