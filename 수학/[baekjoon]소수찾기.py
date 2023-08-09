# ----------------------------------------------------------------------------
# [baekjoon] 소수찾기(수학, python)
# ----------------------------------------------------------------------------
import sys
import math
input = sys.stdin.readline

def prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        # 소수가 아니라면 넘어감
        if x%i==0:
            return False 
    return True


n = int(input())
cnt = 0
# 주어진 수 리스트
arr = list(map(int, input().split()))


for i in range(len(arr)):
    # 1제외 하기
    if arr[i] == (1 or 0):
        continue

    if prime(arr[i]):
        cnt += 1

print(cnt)
