# ----------------------------------------------------------------------------
# [baekjoon_1913] 달팽이(구현,python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n = int(input().rstrip())
target = int(input().rstrip())

# 이차원 리스트 생성
arr = [[0]*n for _ in range(n)]

i, j = 0, 0

# 리스트 값으로 기록할 숫자
count = n*n

def curvied(i, j, length, count):
    # 재귀 탈출 조건
    if (i == n//2) and (j == n//2):
        arr[i][j] = count
        return
    
    # 처음시작값이 고정값으로 이용되기때문에 저장
    row, col = i,j
    
    # 좌(행인덱스 +1, 열인덱스 고정0)
    while i < length:
        arr[i][j] = count
        i += 1
        count -= 1
    i -= 1
    j += 1  # 오른쪽이동

    # 아래
    while j < length:
        arr[i][j] = count
        j += 1
        count -= 1
    i -= 1
    j -= 1  # 위쪽으로

    # 오른쪽
    while i > row-1:
        arr[i][j] = count
        i -= 1
        count -= 1
    i += 1
    j -= 1 # 왼쪽으로

    # 위
    while j > col:
        arr[i][j]= count
        j -= 1
        count -= 1
    
    curvied(row+1, col+1, length-1, count)

curvied(0,0,n, count)

result = []
for row in range(n):
    for col in range(n):
        print(arr[row][col], end=" ")
        if arr[row][col] == target:
            result.append([row+1, col+1])

    print()
print(*result[0])