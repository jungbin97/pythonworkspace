# ----------------------------------------------------------------------------
# [baekjoon_1260] DFS와 BFS(dfs,bfs, python)
# ----------------------------------------------------------------------------
import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().strip().split())

graph = [[] for i in range(n+1)]

# 간선 입력 받기
for _ in range(m):
    a, b = map(int, input().rstrip().split())

    # 간선은 서로 양방향이다.
    graph[a].append(b)
    graph[b].append(a)
    
# 정점이 작은 것 먼저 방문하기 위해
for i in graph:
    i.sort()


def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    # 시작 노드 방문 처리
    for i in graph[v]:
        if visited[i] != 1:
            dfs(i)
            
def bfs(v):
    q = deque([v])
    # 해당 노드 방문 처리
    visited[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] != 1:
                visited[i] = 1
                q.append(i)

visited = [0] * (n+1)
dfs(v)
print()

# BFS처리
visited = [0] * (n+1)
bfs(v)
