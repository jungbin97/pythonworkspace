# ----------------------------------------------------------------------------
# [baekjoon_17086] 아기 상어2
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 8
d = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

tmp = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tmp.append((i, j, 1))

q = deque(tmp)
def bfs():
    while q:
        x, y, cnt = q.popleft()

        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            # out of range
            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny, cnt+1))


bfs()

result = 0
for i in graph:
    result = max((result, max(i)))

print(result-1)