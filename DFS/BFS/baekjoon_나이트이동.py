# ----------------------------------------------------------------------------
# [baekjoon_7562] 나이트 이동(bfs, python) 
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline


# 테스트 케이스 입력
for _ in range(int(input())):
    l = int(input())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())

    visited = [[0]*l for _ in range(l)]
    

    # 시작 노드 큐 삽입
    q = deque([(startX, startY, 0)])
    # 시작 노드 방문 처리
    visited[startX][startY] = 1

    while q:
        x, y, cnt = q.popleft()

        # 탈출 조건
        if x == endX and y == endY:
            print(cnt)
            break
        # 나이트의 이동방향 8방향
        for dx, dy in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
            nx = dx + x
            ny = dy + y
            # 인덱스 범위 체크 and 방문하지 않은 곳
            if 0<= nx < l and 0<= ny < l and visited[nx][ny] == 0:
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = 1
