# ----------------------------------------------------------------------------
# 내장 함수 combinations을 사용해 모든 경우의 수 탐색(완전 탐색)
# ----------------------------------------------------------------------------
import sys
from itertools import combinations

for test_case in range(1, int(input())+1):
    # N : 자연수 개수, K : 합이 되는 수
    N, K = map(int, input().split())

    num = list(map(int, input().split()))

    answer = 0
    for i in range(1, N+1):
        combs = list(combinations(num, i))
        for com in combs:
            if sum(com) == K:
                answer += 1

    print("# {} {}".format(test_case, answer))