# ----------------------------------------------------------------------------
# [baekjoon] 리모컨 (그리디, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

broken = list(map(int, input().split()))

# 현재 채널에서 +, -로만 이동한 횟수
min_count = abs(100 - n)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장났으면 break
        if int(nums[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif  j == len(nums) - 1:
            min_count = min(min_count, abs(n - int(nums))+len(nums))    # 처음에 +, -로만 이동한 경우와, 목표치와 가장 가까운 숫자에서 +,-이동한거리 + 정상입력한 값숫자 개수

print(min_count)