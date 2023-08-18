# ----------------------------------------------------------------------------
# [baekjoon_2615] 오목 (구현-시뮬레이션, python) 

# 현재 바둑독은 왼쪽 맨위 기준 -> 대각선 오른쪽 위로(⬈ -1, 1), 오른쪽(➞ 0, 1), 대각선 오른쪽 아래(⬊ 1,1), 아래(↓ 1,0)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]

# 바둑판 초기화
# for _ in range(19):
#     arr.append(list(map(int, input().split())))

d = [(-1,1), (0,1), (1,1), (1, 0)]

def check():
    for x in range(19):
        for y in range(19):
            if not arr[x][y]:
                continue
            start = arr[x][y]
            for k in range(4):
                nx = x + d[k][0]
                ny = y + d[k][1]
                count = 1

                while 0 <= nx < 19 and 0<= ny < 19 and arr[nx][ny] == start:
                    count += 1
                    if count == 5:
                        # 육목 해당 체크
                        # 시작돌 이전 돌 체크
                        befor_x, befor_y = x - d[k][0], y - d[k][1]
                        if 0<= befor_x < 19 and 0 <= befor_y < 19 and arr[befor_x][befor_y] == start:
                            break

                        # 마지막 돌에서 다음 돌 체크
                        next_x, next_y = nx + d[k][0], ny + d[k][1]
                        if 0<= next_x < 19 and 0 <= next_y < 19 and arr[next_x][next_y] == start: # 같은 돌 색인지 체크
                            break
                        print(start)
                        print(x+1, y+1)
                        return
                    # 오목이 아니면
                    nx += d[k][0]
                    ny += d[k][1]
    print(0)

check()