# ----------------------------------------------------------------------------
# [baekjoon_14940] 쉬운최단거리 (python) 
# ----------------------------------------------------------------------------
from collections import deque

import sys
input = sys.stdin.readline

# 지도는 n, m다름 (정방행렬 X)
n, m = map(int, input().split())

graph = []

# 지도 초기화
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 거리 입력 할 리스트
distance = [[-1]*m for _ in range(n)]

# 목표 지점 찾기(2인 값)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            target = (i,j)
            break
    

q = deque([target])
distance[target[0]][target[1]] = 0

while q:
    x, y = q.popleft();

    # 상 하 좌 우 
    for dx, dy in [(-1,0), (1,0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy

        # 인덱스 범위 체크
        if nx < 0 or nx >=n or ny <0 or ny >=m:
            continue
        
        # 갈 수 있는 땅(1) and 방문하지 않은 곳
        if graph[nx][ny] == 1 and distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()