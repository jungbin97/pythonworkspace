import sys
input = sys.stdin.readline

N = int(input())

T = [0]*(N+1)
P = [0]*(N+1)

# dp table
dp = [0]*(N+1)

for i in range(N):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

# 마지막 인덱스 하나 앞에 ~ 0까지(역순)
for i in range(len(T)-2, -1, -1): 
    if T[i] + i <= N:
        dp[i] = max(dp[i+1], dp[T[i]+i] + P[i])
    else:
        dp[i] = dp[i+1]

print(dp[0])