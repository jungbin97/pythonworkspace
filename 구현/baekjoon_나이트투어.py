# ----------------------------------------------------------------------------
# [baekjoon] 나이트 투어(구현, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

knight_moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, -2), (-1, 2), (-2, 1), (-2, -1)]

answer = "Valid"
visited = []
start = None
for i in range(36):
    now = input().strip()
    now_coord = (ord(now[0]) - 65, int(now[1])- 1)

    # 첫 위치 저장
    if i == 0:
        start = now_coord

    if now_coord in visited:
        answer = "Invalid"
        break
    else:
        visited.append(now_coord)

    if i > 0:
        valid_move = False
        for move in knight_moves:
            expected_position = (prev_coord[0] + move[0], prev_coord[1] + move[1])
            if expected_position == now_coord:
                valid_move = True
                break
        if not valid_move:
            answer = "Invalid"
            break

    prev_coord = now_coord
        
# 마지막 위치에서 시작위치로 이동가능한지 확인
if answer == "Valid":
    valid_end_move = False
    for move in knight_moves:
        expected_position = (prev_coord[0] + move[0], prev_coord[1] + move[1])
        if expected_position == start:
            valid_end_move = True
            break
    if not valid_end_move:
        answer = "Invalid"

print(answer)

# 체스에서 나이트의 이동할 수 있는 곳을 알려주지 않는 불친절한 문제이다.
# 나이트는 "L" 자로만 이동 가능하다.
# (1, 2), (1, -2), (2, 1), (2, -1), (-1, -2), (-1, 2), (-2, 1), (-2, -1)

# Invalid 판정 조건
# 첫번째 : 위에 해당 하는 나이트 이동 조건을 만족하지 않는 경우
# 두번째 : 방문했던 곳을 또 방문하는 경우
# 세번째 : 마지막까지 이동을 마친 자리에서 한번 움직여서(나이트 이동으로) 처음 출발 위치로 복귀 할 수 없는 경우