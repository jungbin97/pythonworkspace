# ----------------------------------------------------------------------------
# [baekjoon_3184] 양
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(r)]
# 방문 체크
visited = [[0]*c for _ in range(r)]
# 상하 좌우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = deque([(x, y)])
    o = 0
    v = 0
    
    # 현재 위치 처리
    visited[x][y] = 1
    if graph[x][y] == "o":
        o += 1
    elif graph[x][y] == "v":
        v += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            # 인덱스 범위 체크
            if 0 <= nx < r and 0<= ny < c and not visited[nx][ny]:
                if graph[nx][ny] == "#":
                    continue
                elif graph[nx][ny] == "v":
                    v += 1
                elif graph[nx][ny] == "o":
                    o += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
    # 양이 더 많으면 늑대 Out
    if o > v:
        return o, 0
    elif v >= o:
        return 0, v

total_sheep = 0
total_wolf = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != "#":
            o, v = bfs(i, j)
            total_sheep += o
            total_wolf += v
            

print(total_sheep, total_wolf)


# 요약
# .(빈필드), #(울타리),  o(양), v(늑대)
# 수평, 수직으로 이동하며 다른 칸으로 이동하면 같은영역 간주
# 영역내에 양>늑대 => 늑대 쫓아냄
# 영역내에 양<=늑대 => 늑대가 모두 먹음

# 풀이
# bfs로 해당 영역의 양, 늑대 갯수 탐색함. 양이 더많으면 o, O