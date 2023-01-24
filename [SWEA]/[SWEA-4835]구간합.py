T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())        # N 입력 받을 숫자 갯수, M 합할 숫자 갯수 

    arr = list(map(int, input().split()))   # 리스트에 숫자입력 

    total = 0

    for number in arr[:M]:
        total += number

    max = min = total

    i = 0
    while M+i < N:
        total -= arr[i]
        total += arr[M+i]

        if total < min:
            min = total
        elif total > max:
            max = total
        i += 1
    

    print("#%d %d" %(test_case, (max-min)))