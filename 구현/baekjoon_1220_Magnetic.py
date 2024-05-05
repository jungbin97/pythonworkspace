# ----------------------------------------------------------------------------
# [swea_1220] 5일차 - Magnetic
# ----------------------------------------------------------------------------
for tc in range(1, 11):
    length = int(input())
    graph = [list(map(int ,input().split())) for _ in range(length)]

    answer  = 0

    for j in range(length):
        state = 0
        for i in range(length):
            # 세로로 탐색
            if graph[i][j] == 1:
                state = 1
            if graph[i][j] == 2 and state == 1:
                answer += 1
                state = 0

    print(f"#{tc} {answer}")


# 요약
# 자성체는 테이블 앞뒤에 있는 N극 S극에만 반응한다.(N은 1, S는 2)
# 윗부분이 N극 아랫부분이 S극