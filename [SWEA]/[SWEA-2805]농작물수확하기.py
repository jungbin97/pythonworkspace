# ----------------------------------------------------------------------------
#  1. 중간지점에서 앞뒤로 한칸씩 증가
#  2. 행 중간에서 한칸씩 작아지도록 앞뒤로 한칸씩 감소
# ----------------------------------------------------------------------------
for test_case in range(1, int(input())+1):
    # 농장의 크기 N
    N = int(input())

    # 농작물 가치
    value = [input() for i in range(N)]
    answer = 0

    # s : 시작 포인트, e : 끝 포인트
    s, e = N//2, N//2
    
    for i in range(N):
        for j in range(s, e+1):
            answer += int(value[i][j])

        # 행의 인덱스가 mid 전까지는 s-e간격 늘리고 mid이후에는 간격 감소
        if i < N // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print("#{} {}".format(test_case, answer))