# ----------------------------------------------------------------------------
# [baekjoon_14719] 빗물 
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

h, w = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
# 인덱스 첫번째, 마지막 미포함(각각 왼쪽기둥 오른쪽기둥 없어서)
for i in range(1, w-1):
    leftCheck = max(max(arr[:i]), arr[i])
    rightCheck = max(max(arr[i+1:]), arr[i])
    
    cnt += min(leftCheck, rightCheck) - arr[i]

print(cnt)