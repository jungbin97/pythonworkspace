# ----------------------------------------------------------------------------
# [baekjoon_2580] 스도쿠 (python, 백트레킹) 
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        # 채워야 할 위치 찾기
        if arr[i][j] == 0:
            zeros.append((i,j))

# 후보 탐색 하기
def candidate(r, c):
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 가로, 세로
    for i in range(9):
        if arr[r][i] in number:
            number.remove(arr[r][i])
        if arr[i][c] in number:
            number.remove(arr[i][c])

    # 3X3
    r, c = r//3, c//3

    for i in range(r*3, (r+1)*3):
        for j in range(c*3, (c+1)*3):
            if arr[i][j] in number:
                number.remove(arr[i][j])
    return number

def dfs(cnt):
    if cnt == len(zeros):
        for row in arr:
            print(*row)
        exit(0)

    i,j = zeros[cnt]
    candi = candidate(i,j)
    for num in candi:
        arr[i][j] = num
        dfs(cnt+1)
        # 후보군을 생성할 수 없는 경우
        arr[i][j] = 0

dfs(0)