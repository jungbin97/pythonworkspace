# ----------------------------------------------------------------------------
# [baekjoon] 랜선자르기(탐색, python)
# ----------------------------------------------------------------------------
import sys

input = sys.stdin.readline

k, n = map(int, input().split())

lan_cable = [int(input()) for _ in range(k)]


answer = 0   # 랜선의 최대 길이

start, end = 1, max(lan_cable)

while start <= end:
    mid = (start+end)//2
    temp_sum = 0
    for i in lan_cable:
        temp_sum += i // mid

    if temp_sum >= n:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)