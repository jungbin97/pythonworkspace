# ------------------- 나눗셈으로 해결 ------------------------
# 나눗셈은 원형큐의 순환을 논리적으로 표현하기 위해 사용한 것
for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))


    print("#{} {}".format(test_case, arr[M % len(arr)])) 
