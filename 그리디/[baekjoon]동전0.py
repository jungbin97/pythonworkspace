# ----------------------------------------------------------------------------
# [baekjoon] 동전0 (그리디, python)
# ----------------------------------------------------------------------------
# import sys
# input = sys.stdin.readline
# n, k = map(int, sys.stdin.readline().split())
# count = 0
# arr = [int(input()) for _ in range(n)]


# for i in range(n-1, -1, -1):
#     count += (k // arr[i])
#     k %= arr[i]
    
# print(count)
# ----------------------------------------------------------------------------
# 가독성 높이기(조건문 추가)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline
n, k = map(int, sys.stdin.readline().split())
count = 0
arr = [int(input()) for _ in range(n)]

for i in range(n-1, -1, -1):
    if arr[i] <= k:
        count += k//arr[i]
        k %= arr[i]

print(count)