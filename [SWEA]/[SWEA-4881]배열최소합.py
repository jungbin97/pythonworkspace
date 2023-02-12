# ---------------N Queen 문제와 유사----------------- 
# BFS로 접근(완전탐색) 백트레킹으로 최적화
# 재귀함수 계산 과정에서 유망한지 지속적으로 판단하고, 다시 원래 지점으로 돌아가는 과정을 그려나갈 수 있어야한다.
# --------------------------------------------------
def back_track(row):
    global part_sum, min_sum
    if part_sum > min_sum:
        return

    if row == N:
        if part_sum < min_sum:
            min_sum = part_sum

    for i in range(N):      # 열체크
        if not visited[i]:
            visited[i] = True  # 현재 열 방문처리
            part_sum += arr[row][i]
            back_track(row+1)  # 아래행으로 이동
            visited[i] = False
            part_sum -= arr[row][i]
       
for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    part_sum = 0
    min_sum = 9999
    back_track(0)
    print("#%d %d" %(test_case, min_sum))