# -------------------- 최단거리 이동은 BFS ---------------------
from collections import deque

def BFS(x, y):
    distance = [[0 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((x, y))

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        x, y = q.popleft()

        if arr[x][y] == 0 or 2:
            arr[x][y] = 1

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0<= nx < N and 0<= ny < N:
                if arr[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 3:
                    return distance[x][y]
    return 0    # 경로가 없는 경우

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 스타트 지점 찾기
    for i in range(N):
        if 2 in arr[i]:
            x = i       # 상, 하 (행)
            y = arr[i].index(2)  # 좌, 우 (열)

    print("#{} {}".format(test_case, BFS(x, y)))
# ------------------------------------------------------------------


# 1. 시작점 좌표찾기
# 2. dfs 함수 거리기록할 distance(이차원 리스트) 생성
# 3. 큐에 시작위치 담음(큐생성)
# 4. 큐에서 하나씩 빼(pop) 0 or 2이면 방문처리 1로 만듬
# 5. 사방으로 갈수 있으므로 체크 후 갈수있으면 distance리스트 방문처리
# 6. 끝점만나면(3)이면 거리를 반환함