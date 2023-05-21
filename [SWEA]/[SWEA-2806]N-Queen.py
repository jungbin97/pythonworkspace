# ----------------------------------------------------------------------------
#  DFS(백트래킹)
# ----------------------------------------------------------------------------
def adjacent(x): # x와 i가 같으면 행이 같음, 근데 for문을 보면 x와 i가 같을 수가 없다.
    for i in range(x):  # 인덱스가 행 row[n]값이 열
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:   # 열이 같거나 대각선이 같으면 false
            return False
    return True

# info : 인덱스, 값 = 행, 몇번쨰 인덱스에 1 넣은지
def dfs(x):
    global result

    # 종료조건 : 마지막행까지 다 퀸을 놓고 왔는지
    if x == N:
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(N):  # i는 열번호 0부터 N전까지 옮겨가면서 유망한곳 찾기
            row[x] = i
            if adjacent(x):     # 행, 열, 대각선 체크함수 true이면 백트래킹 안하고 계속 진행
                dfs(x+1)

for test_case in range(1, int(input())+1):
    N = int(input())
    result = 0

    # row = [1, 3, 0, 2] 0행의 1열, 1행의 3열에 퀸 위치
    row = [0] * N

    dfs(0)
    print("#{} {}".format(test_case, result))