# ----------------------------------------------------------------------------
# [baekjoon_18428] 감시 피하기
# ----------------------------------------------------------------------------
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())

graph = [list(input().split()) for _ in range(N)]

teacher = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == "T":
            teacher += 1
        
# 선생님 이동 방향 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 4가지 방향 직선 체크
def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 직선 방향으로 확인
        while 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != "O":
            if graph[nx][ny] == "S":
                return True
            else:
                nx += dx[i]
                ny += dy[i]
    return False

# 벽 세우기
def back_track(count):
    global answer
    if answer:
        return

    if count == 3:
        T_count = 0
        
        for i in range(N):
            for j in range(N):
                if graph[i][j] == "T":
                    if check(i, j):
                        return
        answer = True
        return


    for i in range(N):
        for j in range(N):
            # 빈공간인것
            if graph[i][j] == "X":
                graph[i][j] = "O"
                count += 1
                back_track(count)
                graph[i][j] = "X"
                count -= 1

answer = False
back_track(0)

if answer:
    print("YES")
else:
    print("NO")


# 요약
# 특정한 위치에 선생님(T), 학생(S), 장애물(O)이 있다.
# 선생님은 상, 하, 좌, 우 4가지 방향으로 감시(단, 복도에 장애물이 있으면 장애물 뒤편에 숨어있는 학생을 볼 수 없다.)
# 3개의 장애물을 설치해서 학생들이 모두 선생님 감시를 피할수 있는지 출력해야한다.(Yes or No)


# # 풀이
# 벽을 새울수 있는 위치에 3개씩 세우고, 모든 학생이 피할 수 있는지 체크합니다. (백트래킹으로 모든 위치를 체크합니다.), 
# 선생님이 탐색할 수있는 4가지 방향에 학생이 존재하는지 체크합니다. (bfs)