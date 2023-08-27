# ----------------------------------------------------------------------------
# [baekjoon_7576] 토마토 (bfs, python) 
# ----------------------------------------------------------------------------
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
tomato = [list(map(int, input().rstrip().split())) for i in range(N)]
date = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if tomato[nx][ny] == 1:
            continue

        if tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            date[nx][ny] = date[x][y] + 1
            q.append((nx, ny))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            sys.exit(0)
result = 0
for i in range(N):
    for j in range(M):
        if result < date[i][j]:
            result = date[i][j]
print(result)