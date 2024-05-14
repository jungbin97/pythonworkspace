# ----------------------------------------------------------------------------
# D3[swea_1873] 상호의 배틀필드
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    # 높이, 너비
    H, W = map(int, input().split())

    graph = [list(input()) for _ in range(H)]

    # 위쪽, 아래쪽, 왼쪽, 오른쪽
    tank = {"^":0,"v":1, "<":2, ">":3, 0:"^", 1:"v", 2:"<", 3:">"}
    # x, y, 방향
    xy_direction = {"U":(-1, 0, 0), "D":(1, 0, 1), "L":(0, -1, 2), "R":(0, 1, 3)}
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 입력 명령에 개수
    N = int(input())
    x, y = 0, 0
    direction = 0
    # 탱크 위치 찾기 및 방향찾기
    found = False
    for i in range(H):
        for j in range(W):
            if graph[i][j] in tank:
                x, y = i, j
                direction = tank[graph[i][j]]
                found = True
                break
        if found:
            break

    command = list(input())
    for comm in command:
        # 방향 체크
        if comm != "S":
            dx, dy, dir = xy_direction[comm]
            nx = x + dx
            ny = y + dy
            # 탱크 방향(이동하지 못해도 방향은 갱신해야함.)
            direction = dir
            # 인덱스 범위 and 평지
            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == ".":
                # 기존위치 평지로
                graph[x][y] = "."
                # 탱크 위치 방향 갱신
                x, y = nx, ny
            graph[x][y] = tank[direction]
        # 포탄이면
        if comm == "S":
            bomb_x, bomb_y = x, y
            while True:
                bomb_x = bomb_x + move[direction][0]
                bomb_y = bomb_y + move[direction][1]
                # 범위를 벗어나거나, 강철벽이면 아무 이벤트 없음.
                if bomb_x < 0 or bomb_y <0 or bomb_x >= H or bomb_y >= W or graph[bomb_x][bomb_y] == "#":
                    break
                # 돌벽 만나면 평지화
                if graph[bomb_x][bomb_y] == "*":
                    graph[bomb_x][bomb_y] = "."
                    break
    print(f"#{tc}", end=" ")
    for row in graph:
        print("".join(row))


# 요약
# 전차 이동시 맵 밖이면 이동하지 않음
# 포탄 발사시 포탄은 벽 충돌하거나 나갈때까지 직진한다.
# 포탄 발사시 벽돌 벽, 강철 벽, 붙이치면 포탄 소멸후 벽돌벽은 평지됨.
# 강철 벽은 아무일도 없음.
