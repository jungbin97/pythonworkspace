# ----------------------------------------------------------------------------
# D2[swea_1959] 백만 장자 프로젝트
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    N = int(input())
    values = list(map(int, input().split()))

    max_value = 0
    result = 0
    for i in range(N-1, -1, -1):
        max_value = max(values[i], max_value)
        if values[i] < max_value:
            result += max_value - values[i]

    print(f"#{tc} {result}")


# 요약
# 원재는 연속된 N일동안 물건의 매매가를 알고있다.
# 하루에 최대 1만큼 구입 가능, 판매할때는 구입 불가

# 풀이
# 배열을 뒤로 탐색하면서 max값 보다 더큰 값은 max 값 갱신
# 현재 위치의 값이 max값 보다 작으면 차익을 결과값에 더해준다.