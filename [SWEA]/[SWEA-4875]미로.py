T = int(input())

def dfs(x, y):
    global result
    graph[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= nx < N) and (0 <= ny < N):
            if graph[nx][ny] == 0:
                dfs(nx, ny)
            if graph[nx][ny] == 3:
                result = 1
                return

for test_case in range(1, T+1):
    N = int(input())    # 미로의 크기 입력
    graph = [list(map(int ,input())) for _ in range(N)]    # 그래프 초기화, 리스트로 변환 숫자 쪼개기 위해
    # visited = [[False for _ in range(N)] for _ in range(N)]    # 방문체크
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]


    # start 지점 찾기 (숫자 2)
    for i in range(N):  # for 연산 한번 줄일수 있다.
        if 2 in graph[i]:
            x = i # 행
            y = graph[i].index(2)  # 열

    result = 0
    dfs(x, y)

    print("#%d %d" %(test_case, result))

        