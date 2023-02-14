# ------------------- 나눗셈으로 해결 ------------------------
for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().splt()))


    print("#{} {}".format(test_case, arr[M % len(arr)])) # 어쩌면 원형큐랑 비슷할지도?

# ------------------- 나눗셈으로 해결 ------------------------
# queue로 해결해보기
