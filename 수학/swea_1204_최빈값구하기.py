# ----------------------------------------------------------------------------
# D2[SWEA_1204] 1일차 - 최빈수 구하기
# ----------------------------------------------------------------------------
from collections import defaultdict

for tc in range(1, int(input())+1):
    t = int(input())

    nums_dict = defaultdict(int)
    nums = list(map(int ,input().split()))

    for num in nums:
        nums_dict[num] += 1
    # 최대 빈도수 찾기
    max_frequency = max(nums_dict.values())

    # 최대 빈도수를 가지는 숫자들 중 가장 큰 수 찾기
    max_num = max(num for num, freq in nums_dict.items() if freq == max_frequency)

    print(f"#{tc} {max_num}")

# 요약
# 최빈수는 특정 자료에서 가장 여러번 나타나는 값을 의미함.

# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
# 최빈수는 8이다.

# 최빈수를 출력하는 프로그램을 작성하라(단 최빈수가 여러개일 때 가장 큰수의 최빈수출력)