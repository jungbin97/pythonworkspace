# 재귀로 구현해야하므로 점화식을 구한다.
def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-1) + paper(n-2)*2

T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 10의 배수 N(가로)
    result = paper(N//10)
    
    print("#{} {}".format(test_case, result))
    