# ----------------------------------------------------------------------------
# [baekjoon_18352] 특정 거리의 도시 찾기
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

INF = float('inf')

N, M, K, X = map(int, input().split())
result = []

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

# 간선 초기화
for _ in range(M):
    A, B = map(int, input().split())
    # 단방향임
    graph[A].append(B)

def bfs(start):
    q = deque()
    q.append((start))
    distance[start] = 0
    while q:
        node = q.popleft()
        if distance[node] == K:
            break;

        # 인접 노드로 이동
        for i in graph[node]:
            if distance[i] == INF:
                distance[i] = min(distance[i], distance[node]+1)
                if distance[i] == K:
                    result.append(i)
                q.append(i)
bfs(X)

if len(result) == 0:
    print(-1)
else:
    for i in sorted(result):
        print(i)

# ----------------------------------------------------------------------------
# 다익스트라
# ----------------------------------------------------------------------------
import sys
import heapq
input = sys.stdin.readline

INF = float('inf')

N, M, K, X = map(int, input().split())
result = []

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

# 간선 초기화
for _ in range(M):
    A, B = map(int, input().split())
    # 단방향임
    graph[A].append((B, 1))

def dijkstra(start):
    # 우선 순위 큐에 삽입(거리, 노드번호)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        # 인접 노드 체크
        for i, cost in graph[node]:
            new_distance = dist + cost
            if new_distance < distance[i]:
                distance[i] = new_distance
                heapq.heappush(q, (new_distance, i))

dijkstra(X)

for i in range(1, N+1):
    if distance[i] == K:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)