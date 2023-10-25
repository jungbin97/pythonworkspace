import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int,input().split())

arr = list(list(map(int, input().split())) for _ in range(n))
house = []
chick = []

# 좌표 뽑기
for i in range(n):
    for j in range(n):
        # 집 좌표
        if arr[i][j] == 1:
            house.append((i+1, j+1))
        # 치킨집 좌표
        elif arr[i][j] == 2:
            chick.append((i+1, j+1))

# 도시 치킨 거리
min_distance = float('inf')

# 각 조합에 대한 도시의 치킨 거리 계산
for chicken in combinations(chick, m):
    distance = 0
    for h_i, h_j in house:
        temp = float('inf')
        for c_i, c_j in chicken:
            temp = min(abs((h_i) - (c_i)) + abs((h_j)-(c_j)), temp)
        distance+=temp
    min_distance = min(min_distance, distance)

print(min_distance)
