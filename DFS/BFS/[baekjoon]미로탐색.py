# ----------------------------------------------------------------------------
# [baekjoon] 미로탐색 (bfs, python) 
# ----------------------------------------------------------------------------
from collections import deque

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input())))
    
# 너비 우선 탐색
def bfs(x, y):
    # 이동 좌표 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()

        # 현재 위치에서 4가지 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 위치 벗어나는지 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if array[nx][ny] == 0:
                continue

            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                q.append((nx, ny))

    return array[n-1][m-1]

print(bfs(0, 0))