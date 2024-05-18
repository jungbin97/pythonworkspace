# ----------------------------------------------------------------------------
# D3[swea_5948] 새샘이의 7-3-5 게임
# ----------------------------------------------------------------------------
from itertools import combinations

for tc in range(1, int(input())+1):
    nums = list(map(int, input().split()))

    result  = set()
    for value in combinations(nums,3):
        result.add(sum(value))

    result = sorted(result, reverse=True)
    print(f"{tc} {result[4]}")


# 요약
# 7개의 정수중 3개의 정수를 골라 합을 구해, 5번째로 큰수를 출력