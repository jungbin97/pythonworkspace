# ----------------------------------------------------------------------------
# [programmers] 
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][1] = i    # i개에서 1개 선택 경우의 수는 i개
    dp[i][0] = 1    # i개에서 1개도 선택핮 않는 경우의 수 0개
    dp[i][i] = 1    # i개에서 모두 선택하는 경우의 수는 1개

for i in range(2, n+1):
    for j in range(2 , i):
        dp[i][j] = dp[i-1][j]+dp[i-1][j-1]

print(dp[n][k])