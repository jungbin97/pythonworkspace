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


# ----------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------

n = int(input())
tar = int(input())
lst = [[0 for _ in range(n)] for _ in range(n)]
r, c = n // 2, n // 2
lst[r][c] = 1
lst[r - 1][c] = 2
lst[r - 1][c + 1] = 3
t = 4
c = c + 1

def down():
    global r, c, t
    while lst[r][c - 1] > 0 and t < (n * n) + 1 :
        lst[r][c] = t
        t += 1
        r += 1
        if r == n:
            r = n - 1
            return

def left():
    global r, c, t
    while lst[r - 1][c] > 0 and t < (n * n) + 1 :
        lst[r][c] = t
        t += 1
        c -= 1
        if c == -1:
            c = 0
            return
    
def up():
    global r, c, t
    while lst[r][c + 1] > 0 and t < (n * n) + 1:
        lst[r][c] = t
        t += 1
        r -= 1
        if r == -1:
            r = 0
            return

def right():
    global r, c, t
    while lst[r + 1][c] > 0 and t < (n * n) + 1:
        lst[r][c] = t
        t += 1
        c += 1
        if c == n:
            c = n - 1
            return
    
while t < (n * n) + 1:
    down()
    left()
    up()
    right()

a, b = 0, 0

for i in range(n):
    for j in range(n):
        if lst[i][j] == tar:
            a = i + 1
            b = j + 1
        print(lst[i][j], end = " ")
    print()

print(a, b)