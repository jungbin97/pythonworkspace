import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N, M = map(int ,input().split())

result = 0
# 상하좌우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# 안전영역 계산
def bfs():
    q = deque()
    # 원래의 arr 복사
    tmp_arr = copy.deepcopy(arr)

    # 바이러스 큐 삽입
    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M: # 범위 확인
                if tmp_arr[nx][ny] == 0: # 감염 가능 확인
                    tmp_arr[nx][ny] = 2
                    q.append((nx, ny))

    global result
    cnt = 0
    for i in range(N):
        cnt += tmp_arr[i].count(0)
    result = max(result, cnt)

def makewall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: # 빈 공간이라면 벽 세우기
                arr[i][j] = 1 # 벽으로 만듬
                makewall(cnt+1)
                arr[i][j] = 0


makewall(0)
print(result)