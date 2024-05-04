# ----------------------------------------------------------------------------
# [baekjoon_1303] 전쟁 - 전투
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

# 가로 세로 크기
n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

my_team = 0
enemy_team = 0


def bfs(i, j, team):
    q = deque([(i, j)])
    visited[i][j] = True
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            # 인덱스 범위 체크
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == team:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))
    return cnt

for i in range(m):
    for j in range(n):
        if graph[i][j] == "W":
            if not visited[i][j]:
                my_team += bfs(i, j, "W")**2
        elif graph[i][j] == "B":
            if not visited[i][j]:
                enemy_team += bfs(i, j, "B")**2

print(my_team, end = " ")
print(enemy_team)

# 요약
# 같은 팀의 병사들이 뭉처있으면 위력이 커진다.

# 내팀 W, 적국 B

# 풀이 
# BFS 탐색으로 계산한다.
