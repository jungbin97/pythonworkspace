#------------------------------------------------------
# [이코테] 효율적인 화폐 구성 (DP : bottom-up)
#------------------------------------------------------
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
money = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# dp 테이블 초기화
d = [10001] * (M+1)

# 0원을 만들기 위해 0개 필요
d[0] = 0

# 작은 문제부터 해결하면서 dp 테이블에 기록(bottom-up)
for i in range(N):
    for j in range(money[i], M+1):
        if d[j - money[i]] != 10001:    # (i-k)을 만드는 방법이 있는경우 a_(i-k) 기본값이 아닌 경우)
            d[j] = min(d[j], d[j-money[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])