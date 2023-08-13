# ----------------------------------------------------------------------------
# [baekjoon_2579] 계단 오르기(DP, python) 
# bottom-up 방식

# dp 테이블과 arr를 가변적으로 두면 => d = [0]*n
# n의 값이 1일경우 18, 19분줄에 배열의 범위를 벗어난 접근을 하게 된다.
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n = int(input().rstrip())

# d = [0]*(n+1)
d = [0]*301
arr = [0]*301

for i in range(n):
    arr[i] = int(input().rstrip())

d[0] = arr[0]
d[1] = arr[0]+arr[1]
d[2] = max(arr[0]+arr[2], arr[1]+arr[2])
for i in range(3, n):
    d[i] = max(d[i-2]+arr[i], d[i-3]+arr[i-1]+arr[i])


print(d[n-1])