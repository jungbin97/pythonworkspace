# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
for _ in range(10):

    tc = int(input())
    # 배열 입력받기 (이중 리스트)
    arr = [list(int(input().split())) for _ in range(100)]
    result = 0
    
    # 가로줄의 합
    max1 = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if sum > max1:
            max1 = sum

    # 세로줄의 합
    max2 = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum = arr[j][i]
        if sum > max2:
            max2 = sum

    # 대각선의 합
    max3 = 0
    for i in range(100):
        sum1, sum2 = 0, 0
        # 오른쪽 대각선 합
        sum1 += arr[i][i]
        sum2 += arr[i][99-i]
    if max(sum1, sum2) > max3:
        max3 = max(sum1, sum2)
        
    print("#{} {}".format(tc, max(max1, max2, max3)))