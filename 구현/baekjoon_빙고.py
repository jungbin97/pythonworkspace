arr = [list(map(int, input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

# 사회자가 숫자 부른 횟수
cnt = 0

def check():
    bingo = 0
    # 가로 체크
    for r in arr:
        if r.count(0) == 5:
            bingo += 1

    # 세로 체크
    for i in range(5):
        temp = 0
        for j in range(5):
            if arr[j][i] == 0:
                temp += 1
        if temp == 5:
            bingo += 1

    # 주대각선 체크, 부대각선 체크
    mainDiagonal = 0
    subDiagoanl = 0
    for i in range(5):
        if arr[i][i] == 0:
            mainDiagonal += 1
        if arr[i][4-i] == 0:
            subDiagoanl += 1

    if mainDiagonal == 5:
        bingo += 1
    if subDiagoanl == 5:
        bingo += 1
    
    return bingo

for i in range(25):
    for x in range(5):
        for y in range(5):
            # 사회자가 부른 숫자와 같으면 0으로 처리
            if arr[x][y] == mc[i]:
                cnt += 1
                arr[x][y] = 0
                if check() >= 3:
                    print(cnt)
                    exit(0)