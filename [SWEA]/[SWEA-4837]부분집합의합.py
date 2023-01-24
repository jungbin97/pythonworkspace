T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A = [i for i in range(1, 13)]   # 리스트 1~12 까지
    length = len(A)

    N, K = map(int, input().split())

    count = 0
    for i in range(1<<length):
        tmp = []    # 부분집합 임시로 저장할 공간
        for j in range(length):
            if i&(1<<j):
                tmp.append(A[j])
        if len(tmp) == N and sum(tmp) == K:     # 부분집합의 조건 확인
            count += 1

    print("#%d %d" %(test_case, count))