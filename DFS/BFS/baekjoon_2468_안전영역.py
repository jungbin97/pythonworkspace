# ----------------------------------------------------------------------------
# [baekjoon_2468] 안전영역
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

max_rain = max(max(row)for row in graph)

def bfs(rain, x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문하지 않았고, 높이가 현재 비의 양보다 크고, 인덱스 범위이내이면 방문처리
            if 0<= nx <n and 0 <= ny <n and visited[nx][ny] == 0 and graph[nx][ny] > rain:
                visited[nx][ny] = 1
                q.append((nx, ny))

result = 0
for rain in range(max_rain+1):
    count = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and visited[i][j] == 0:
                bfs(rain, i, j, visited)
                count += 1

    result = max(result, count)


print(result)

# 요약  
# 비의 양에 따른 모든 경우의 조사하고
# 물이 잠기지 않는 안전영역의 최대 개수 찾아라



# 풀이
# 비의 양은 모든 높이 정보의 0 ~ 최대값까지의 범위이다.
# 해당 비의 양보다 큰 곳의 영영을 bfs로 상하 좌우 체크한다. 체크하고 count + 1, 방문처리해준다.
# 반환된 Count가 최대인 수를 출력한다.