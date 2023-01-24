#N입력 받기 
n = int(input())
x, y = 1,1
plans = input().split()

#L, R, U, D 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_tpyes = ['L', 'R', 'U', 'D']


#이동 계획 설계
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_tpyes)):
        if plan == move_tpyes[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어난 경우 확인
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #이동 수행
    x, y = nx , ny

print(x, y)