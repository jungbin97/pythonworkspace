# ----------------------------------------------------------------------------
# [baekjoon_2615] 오목 (구현-시뮬레이션, python) 

# 현재 바둑독은 왼쪽 맨위 기준 -> 대각선 오른쪽 위로(⬈ -1, 1), 오른쪽(➞ 0, 1), 대각선 오른쪽 아래(⬊ 1,1), 아래(↓ 1,0)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

arr = []

# 바둑판 초기화
for _ in range(19):
    arr.append(list(map(int, input().split())))

def check():
    for x in range(19):
        for y in range(19):
            if arr[x][y] != 0:
                for dx, dy in [(-1,1), (0,1), (1,1), (1, 0)]:
                    nx = x + dx
                    ny = y + dy
                    count = 1

                    while 0 <= nx < 19 and 0<= ny < 19 and arr[nx][ny] == arr[x][y]:
                        count += 1
                        if count == 5:
                            # 육목 해당 체크
                            # 시작돌 이전 돌 체크
                            befor_x, befor_y = x - dx, y - dy
                            if 0<= befor_x < 19 and 0 <= befor_y < 19 and arr[befor_x][befor_y] == arr[x][y]:
                                break

                            # 마지막 돌에서 다음 돌 체크
                            next_x, next_y = nx + dx, ny + dy
                            if 0<= next_x < 19 and 0 <= next_y < 19 and arr[next_x][next_y] == arr[x][y]: # 같은 돌 색인지 체크
                                break
                            print(arr[x][y])
                            print(x+1, y+1)
                            return
                        # 오목이 아니면
                        nx += dx
                        ny += dy
    print(0)

check()


