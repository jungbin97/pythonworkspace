# ----------------------------------------------------------------------------
# D3[SWEA_5215] 햄버거 다이어트
# ----------------------------------------------------------------------------
from itertools import combinations
for tc in range(1, int(input())+1):
    # 재료수, 제한 칼로리
    N, L  = map(int, input().split())
    answer = 0

    # 재료리스트(맛 점수, 칼로리)
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(1, N+1):
        for per in combinations(ingredient, i):
            sum_calorie = 0
            sum_taste = 0
            for taste, calorie in per:
                sum_calorie += calorie
                sum_taste += taste
            # 제한 칼로리를 넘으면 현재 조합 탈출
                if sum_calorie > L:
                    break
            if sum_calorie <= L:
                answer = max(answer, sum_taste)
                    
    print(f"#{tc} {answer}")


# 요약
# 제한된 칼로리 L 이하 이면서 가장 가장 맛에 대한 점수가 높은 햄버거의 점수를 반환하라. (같은 재료를 여러번 사용불가)
# 풀이
# 20C1 + 20C2 + 20C3 + ... + 20C20 = 약 10만번