# ----------------------------------------------------------------------------
# [baekjoon_3085] 사탕 게임 
# ----------------------------------------------------------------------------
import sys
iunput = sys.stdin.readline

N = int(input())

graph = [list(input()) for _ in range(N)]

# 오른쪽과 아래만 체크해도됨
d = [(1, 0), (0, 1)]
answer = 0

def check():
    max_count = 1
    for i in range(N):
        cnt = 1
        # 행 체크 
        # out of range 방지로 2번쨰것 부터 체크
        for j in range(1, N):
            if graph[i][j] == graph[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_count = max(max_count, cnt)
        
        # 열 체크
        cnt = 1
        for j in range(1, N):
            if graph[j][i] == graph[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_count = max(max_count, cnt) 
    return max_count

for x in range(N):
    for y in range(N):
        for direction in d:
            nx = x + direction[0]
            ny = y + direction[1]
            # 범위 체크
            if 0 <= nx < N and 0 <= ny < N:
                if graph[x][y] != graph[nx][ny]:
                    # swap 해줌
                    graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                    answer = max(answer, check())
                    # 원상 복귀
                    graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
    
print(answer)

# 요약
# 인접한 색이 다른 사탕 2개 고름
# 서로 교환
# 모두 같은 색으로 이루어져있는 가장 긴 연속 부분(행, 열) 모두 먹는다.

# 상근이가 먹을 수 있는 사탕의 최대 개수를 구하여라
# C빨강, P 파란, Z초록, Y노랑


# 풀이
# 현재 위치에서 상하 좌우 같지 않은 사탕 있는지 확인
# 같지 않으면 swap

