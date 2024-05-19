# ----------------------------------------------------------------------------
# [baekjoon_11725] 트리의 부모 찾기
# ----------------------------------------------------------------------------
from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)


for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = deque()
q.append(1)
def bfs():
    while q:
        node = q.popleft()

        for next_node in graph[node]:
            if visited[next_node] == 0:
                visited[next_node] = node
                q.append(next_node)

bfs()
# 2번 노드부터 출력
for i in visited[2:]:
    print(i)


# 풀이
# 1번에서 스타트, 구할 노드의 이전 노드를 찾자.
# dfs일경우 100,000번째 재귀를 찾을수도있음.
# bfs로?
# 이동하기전 노드(루트 노드)를 저장한다.

# 풀이
# 간선에 방향이 없는 무방향 그래프 이므로 양방향으로 초기화해야함.
# 노드1 부터 시작하여 모든 노드에 대해서 초기화한다.
# 큐에 추가하기전에 현재 노드를 visited[next_node] = node 하면 vsited에는 이전 노드가 기록됨
