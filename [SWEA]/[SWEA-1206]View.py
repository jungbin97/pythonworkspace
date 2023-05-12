# ----------------------------------------------------------------------------
# 조망권의 개수 : 자기 높이 - 주변 4개 빌딩 중 가장 큰 빌딩
# ----------------------------------------------------------------------------

for test_case in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    # 조망권이 확보된 세대 수
    count = 0

    for i in range(2, N-2):
        m = max(height[i-1], height[i-2], height[i+1], height[i+2])
        if height[i] > m:
            count += height[i] - m 


    print("#{} {}".format(test_case, count))