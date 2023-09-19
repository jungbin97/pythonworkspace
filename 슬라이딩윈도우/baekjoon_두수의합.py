# ----------------------------------------------------------------------------
# [baekjoon_3273] 두수의 합 
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

target = int(input())

start = 0
end = len(arr) -1

result = 0
while start < end:
    part_sum = arr[start] + arr[end]
    if part_sum == target:
        result += 1
        start += 1
    # 값을 줄여줘야 함.
    elif part_sum > target:
        end -= 1
    # 값을 늘려줘야 함.
    elif part_sum < target:
        start += 1

print(result)

# ----------------------------------------------------------------------------
# hash 사용
# ----------------------------------------------------------------------------

n = int(input())
arr = list(map(int,input().split()))
target = int(input())

dic = {}
for num in arr:
    dic[num] = dic.get(num, 0) + 1

result = 0
for num in arr:
    temp = target - num
    if temp in dic:
        result += 1
        # 같은 수 중복 제거
    if temp == num:
        result -= 1

print(result // 2)