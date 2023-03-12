# -------------------------------------------------
#  [이코테] 개미전사 (DP)
# -------------------------------------------------

# N = int(input())
# arr = list(map(int, input().split()))

# d = [0] * 100   # DP 테이블

# d[0] = arr[0]
# d[1] = max(arr[0], arr[1])

# for i in range(2, N):
#     d[i] = max(d[i-1], d[i-2] + arr[i])

# print(d[N-1])

# -------------------------------------------------
#  입력 시간 초과 개선
# -------------------------------------------------
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0] * 100   # DP 테이블

d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[N-1])