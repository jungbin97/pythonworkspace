# ----------------------------------------------------------------------------
# [baekjoon] 소수구하기(수학_ 에라토스테네스의 채, python)
# ----------------------------------------------------------------------------
import sys
import math
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [i for i in range(n+1)]    # 0~16
arr[1] = 0

for i in range(2, int(math.sqrt(n))+1):
    # 소수가 아니면 넘어감
    if arr[i]==0:
        continue
        # 소수의 배수 값을 N까지 반복
    for j in range(i+i, n+1, i):
        arr[j] = 0
            
for i in range(m, n+1):
    if arr[i] != 0:
        print(arr[i])