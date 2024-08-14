# ----------------------------------------------------------------------------
# [baekjoon_11060] 점프점프
# ----------------------------------------------------------------------------
n = int(input())
A = list(map(int, input().split()))


dp = [1e9] * n
dp[0] = 0

for i in range(n):
    for j in range(1, A[i]+1):
        if i+j < n:
            dp[i+j] = min(dp[i]+1, dp[i+j])

if dp[-1] == 1e9:
    print(-1)
else:
    print(dp[-1])