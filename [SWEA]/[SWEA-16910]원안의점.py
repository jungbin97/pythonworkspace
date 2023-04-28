# ----------------------------------------------------------------------------
# [SWEA-16910][D3] 원안의 점
# 1. 완전탐색 방식
# 2. 모든 경우의 수(x,y) 조합을 확인
# 시간 복잡도 : O(N^2)
# ----------------------------------------------------------------------------
import math

for test_case in range(1, int(input()) + 1):
    N = int(input())
    x = list(range(-N, N+1))
    y = list(range(-N, N+1))
    cnt = 0
    for i in x:
        for j in y:
            if math.sqrt(pow(i, 2) + pow(j, 2)) <= N:
                cnt += 1
                    
    print("#%d %d"%(test_case, cnt))

    
                    