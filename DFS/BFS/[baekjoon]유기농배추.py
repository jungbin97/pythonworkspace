# ----------------------------------------------------------------------------
# [baekjoon] 유기농 배추(dfs, python)
# ----------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
#   # 상하좌우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <=nx < n) and (0 <=ny < m):
            if arr[nx][ny] == 1:
                arr[nx][ny] = -1
                dfs(nx , ny)


test_case = int(input())

for _ in range(test_case):
    m, n, k = map(int, input().split())
    cnt = 0

    arr = [[0]*m for _ in range(n)]


    # 배추 위치 지정
    for i in range(k):
        r, l = map(int, input().split())
        arr[l][r] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                dfs(i, j)
                cnt += 1

    print(cnt)