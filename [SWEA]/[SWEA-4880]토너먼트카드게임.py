def div_con(start, end):
    if start == end:    #  재귀 탈출 조건
        return start

    a = div_con(start, (start+end)//2)
    b = div_con((start+end)//2 + 1, end)    
    return rsp(a, b)    # 인덱스 번호만 반환하여 연산

def rsp(x, y):
    if cards[x] == cards[y]:    # 비긴 경우
        return x
    elif cards[x] - cards[y] == -2 or cards[x] - cards[y] == 1:
        return x
    return y



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    print("#{} {}".format(test_case, div_con(0, N-1)+1))