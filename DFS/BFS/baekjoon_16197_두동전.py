# ----------------------------------------------------------------------------
# [baekjoon_16197] 두 동전
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline
# 세로, 가로
n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(n)]

# 상, 하, 좌, 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

coins = deque()
def bfs():
    while coins:
        x1, y1, x2, y2, count = coins.popleft()
        if count >= 10:
            return -1

        for dx, dy in d:
            nx1 = x1 + dx
            ny1 = y1 + dy
            nx2 = x2 + dx
            ny2 = y2 + dy
            
            # 범위체크
            if 0 <= nx1 < n and 0 <= ny1 < m and 0<= nx2 < n and 0<= ny2 < m:
                # 범위 안이지만 벽일경우
                if graph[nx1][ny1] == "#":
                    nx1 = x1
                    ny1 = y1
                if graph[nx2][ny2] == "#":
                    nx2 = x2
                    ny2 = y2
                coins.append((nx1, ny1, nx2, ny2, count+1))
            # coin2가 떨어진경우
            elif 0 <= nx1 < n and 0 <= ny1 < m:
                return count + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:
                return count + 1
            # 둘다 빠진경우
            else:
                continue
    return -1

tmp = []
for i in range(n):
    for j in range(m):
        # 동전이면 좌표 찾기
        if graph[i][j] == "o":
            tmp.append((i, j))

coins.append((tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1], 0))

print(bfs())

# 요약
# 두 동전을 이동하는 문제, 각칸은 비어있거나, 벽이다.
# 두 동전은 동시에 해당 방향으로 이동한다.

# 동전이 이동하는 칸이 벽이면 동전은 이동하지 않음.
# 동전이 이동하는 칸에 칸이없으면(out of range)이면 보드 바깥으로 떨어짐.
# 이동하려는 칸에 동전이 있는 경우에도 한칸 이동함.

# 두동전중 하나만 보드에서 떨어뜨리기위한 최소 버튼 누르는 횟수를 구하여라

# 풀이
# 하나만 out of range할경우 어떻게 처리할지? => count+1를 반환하고 종료한다.
# 둘중하나가 벽을 마주한다면? => 이동하려는 곳이 벽(#)이라면 현재 좌표로 유지함.