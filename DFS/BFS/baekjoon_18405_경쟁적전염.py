# ----------------------------------------------------------------------------
# [baekjoon_18405] 경쟁적 전염
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

s, result_x, result_y = map(int, input().split())

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j], i, j, 0))
# 바이러스 번호가 작은순으로 정렬
q.sort()
q = deque(q)

# BFS
while q:
    virus, x, y, time = q.popleft()
    # 시간이 s 만큼 지나면 중단
    if time == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스 범위 체크
        if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
            continue
        # 아직 바이러스가 방문하지 않았다면
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, nx, ny, time+1))

print(graph[result_x-1][result_y-1])
# 요약
# 바이러스는 1~K번까지 K가지 종류가 있다.

# 바이러스는 1초마다 상하좌우 방향으로 증식, 전부 증식하나, 매번 번호가 낮은 바이러스 먼저 증식한다.
# 증식과정에서 이미 어떤 바이러스가 있으면 그위치는 증식 불가

# S초가 지난후 (X,Y)에 존재하는 바이러스의 종류를 출력하라.

# 풀이
# BFS로 인접 노드를 번호가 낮은 바이러스 순서대로 큐에 넣는다.(바이러스 종류, 좌표, 시간)
# 그러면 증식 순서도 보장된다.
# 해당 위치가 0이 아니면 이미 다른 바이러스가 증식한 부분이므로 건너뛴다.
# S시간 되면, X, Y 위치의 바이러스번호를 출력한다.