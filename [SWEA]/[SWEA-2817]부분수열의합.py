# ----------------------------------------------------------------------------
# 내장 함수 combinations을 사용해 모든 경우의 수 탐색(완전 탐색)
# 시간 초과발생 
# ----------------------------------------------------------------------------
# import sys
# from itertools import combinations

# for test_case in range(1, int(input())+1):
#     # N : 자연수 개수, K : 합이 되는 수
#     N, K = map(int, input().split())

#     num = list(map(int, input().split()))

#     answer = 0
#     for i in range(1, N+1):
#         combs = list(combinations(num, i))
#         for com in combs:
#             if sum(com) == K:
#                 answer += 1

#     print("# {} {}".format(test_case, answer))

# ----------------------------------------------------------------------------
# 백트래킹 기법 사용
# 현재 숫자를 포함하는 경우와 포함하지 않는 경우나눠서 idx끝까지 경우의 수 탐색
# 탈출조건 : S값에 도달, idx 범위 초과
# ----------------------------------------------------------------------------
import sys

for test_case in range(1, int(input())+1):
    # N : 자연수의 개수, K : 합이되는 수
    N, S = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    count = 0

    def backTracking(sum, idx):
        global count
        if idx >= N:
            return
        sum += nums[idx]
        if sum == S:
            count += 1

        # 현재 숫자를 포함하는 경우
        backTracking(sum, idx+1)
        # 현재 숫자를 포함하지 않는 경우
        backTracking(sum-nums[idx], idx+1)
    
    backTracking(0,0)
    print("#{} {}".format(test_case, count))

