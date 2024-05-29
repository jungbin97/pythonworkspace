# ----------------------------------------------------------------------------
# [baekjoon_16236] 아기 상어 
# ----------------------------------------------------------------------------
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# 아기상어의 이동방향(상하좌우)
d = [(-1, 0), (1, 0),(0, -1),(0, 1)]

# 아기상어 위치 
def find_baby_shark():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                graph[i][j] = 0
                return (i, j)
            
            
# 아기상어가 먹을 수 있는 물고기 찾기
# dfs사용
def priority_baby_shark(x, y, baby_shark_size):
    # 행, 열, 거리
    q = deque([(x, y, 0)])
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True

    fishs = []

    while q:
        cx, cy, dist = q.popleft()

        for dx, dy in d:
            nx = cx+dx
            ny = cy+dy
            # 인덱스 범위 이내, 방문하지 않은곳
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 아기상어 크기보다 작은 곳 
                if graph[nx][ny] <= baby_shark_size:
                    visited[nx][ny]=True
                    # 그중 물고기만
                    if 0 < graph[nx][ny] < baby_shark_size:
                        fishs.append((dist+1, nx, ny))
                    else:
                        q.append((nx, ny, dist+1))

    if fishs:
        fishs.sort()
        return fishs[0]
    else:
        None
            

# 아기상어 이동
def move_baby_shark():
    # 아기상어 위치
    x, y = find_baby_shark()
    # 아기 상어 크기
    baby_shark_size = 2
    # 초
    time = 0
    # 먹은 물고기 개수
    cnt = 0
    
    # 시뮬레이션 시작
    while True:
        # 이동 가능한 곳 우선순위 지정
        tmp = priority_baby_shark(x, y, baby_shark_size)
        # 이동 가능한 곳이 없으면 종료
        if tmp is None:
            break
        
        dist, nx, ny = tmp
        time += dist
        # 이동한 칸은 빈칸으로 처리
        graph[nx][ny] = 0
        # 아기상어 위치 갱신
        x, y = nx, ny
        # 먹은 물고기 개수 증가
        cnt += 1
        
        # 아기상어 크기 증가
        if cnt == baby_shark_size:
            baby_shark_size += 1
            cnt = 0

    return time

print(move_baby_shark())


# 요약
# 아기상어 초기 값 : 크기2, 초 0, 먹은 물고기 횟수 0

# - 자기보다 크기가 큰 물고기 칸 이동불가
# - 자기보다 같은 크기 이동 가능, 못먹음.
# - 자기보다 작은 크기 물고기 이동 가능, 먹을수 있음

# 아기상어 이동 우선순위
# - 거리가 가장 가까운 물고기(이동할떄 지나가야하는 칸의 개수 최소)
# - 거리가 동일할경우, 행이 작은 물고기, 열이 작은 물고기 선택

# 물고기를 먹으면 그칸은 이동할 수 있는 빈칸이 됨.
# 아기상어는 자신으 크기와 같은 물고기 횟수를 먹을때마다 크기가 1증가한다.

# 몇초동안 몰고기를 잡아먹을 수 있는지 출력하라.