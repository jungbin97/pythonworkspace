T = int(input())

for test_case in range(1, T+1):
    
    N = int(input())
    ai = list(map(int, input().split()))

    ai.sort()   # 오름차순 정렬
    tmp = []    # 리스트에서 뽑은 숫자 저장

    for i in range(0, N//2):
        tmp.append(ai[N-1-i])
        tmp.append(ai[i])

    print("#%d" %test_case, end=" ")
    for i in range(10):
        print(tmp[i], end = " ")
    print()

    