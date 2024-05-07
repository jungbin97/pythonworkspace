# ----------------------------------------------------------------------------
# [baekjoon_1743] 음식물 피하기
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

# 세로길이, 가로길이, 음쓰 개수
n, m, k = map(int, input().split())

# 음쓰 있는것 2, 없는 곳 1
graph = [[1]*m for _ in range(n)]
# 방문체크 리스트
visited = [[False]*m for _ in range(n)]

# 상하좌우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

result = 0
def bfs(i, j):
    q = deque([(i,j)])
    visited[i][j] = True
    cnt = 1
    
    while q:
        x,y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            # 인덱스 범위 체크, 방문 하지 않았다면, 음쓰면
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 2:
                cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return cnt

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 2

for i in range(n):
    for j in range(m):
        # 음쓰고 방문하지 않는 곳이면 bfs 진행
        if graph[i][j] == 2 and not visited[i][j]:
            result = max(result, bfs(i, j))

print(result)

# 요약
# 음식물중 가장 큰 음식물의 크기를 구하여라(대각선으로는 음식물이 붙을 수 없고 상하좌우로만 붙을 수 있음)