# --------------------- 단순 리스트 insert 함수로 구현 --------------------------
for test_case in range(1, int(input())+1):
    N, M, L = map(int, input().split())   # N 수열의 길이 M 추가횟수 L 출력할 인덱스 번호
    arr = list(map(int, input().split()))

    for _ in range(M):
        idx, value = map(int, input().split())
        arr.insert(idx, value)
    print("#{} {}".format(test_case, arr[L]))
# ------------------------------------------------------------------------------
# 연결 리스트로 구현
