# ----------------------------------------------------------------------------
# [이코테] 치킨배달 (구현, python)
# ----------------------------------------------------------------------------
from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1: # 집일 때
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

# 전체 치킨집에서 M개를 뽑는 조합 계산
chickenComb = (list(combinations(chicken, m)))

# 도시의 치킨 거리 최소 값 구하기 위해 초기 최대 변수 설정
result = int(1e9)

for i in chickenComb:
    # 도시의 치킨거리를 계산하기 위한 변수
    city_chicken_dist = 0

    for j in house:
        # 최소 치킨 거리 구하는 변수
        chicken_didst = int(1e9)

        for x, y in i:
            # 각집에서 치킨 집 거리 비교
            chicken_didst = min(chicken_didst, abs(j[0]-x) + abs(j[1]-y))

        # 해당 집의 치킨거리를 도시 치킨거리에 합침
        city_chicken_dist += chicken_didst
    
    # 치킨집 조합에 따른 도시 치킨 거리에서 최소 추출
    result = min(result, city_chicken_dist)

print(result)