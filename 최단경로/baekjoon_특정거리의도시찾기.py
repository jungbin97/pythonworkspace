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