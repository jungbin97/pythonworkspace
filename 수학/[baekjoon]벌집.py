# ----------------------------------------------------------------------------
# [baekjoon_2292] 벌집 (수학,python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n = int(input())

house = 1
cnt = 1

while n > house:
    house += 6*cnt  # 벌집 6의 배수로 증가
    cnt += 1

print(cnt)