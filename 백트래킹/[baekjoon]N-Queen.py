n = int(input())
result = 0
row = [0] * n
# 인덱스를 행, 값을 열로 사용
# 같은 열일떄 row[x] == row[i]
# 대각선일 떄 : abs(row[x] - row[i]) = x - i
def adjacent(x):
    for i in range(x):      # 인덱스가 행, 값이 열
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:      # 열이 같거나 대각선이 같으면
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        # 각행에 퀸 놓기
        for i in range(n):  # 해당 행의 열을 차례대로 탐색하여 유망한곳 찾기
            row[x] = i
            if adjacent(x):
                dfs(x+1)


dfs(0)
print(result)