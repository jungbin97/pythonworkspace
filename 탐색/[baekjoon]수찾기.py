# ----------------------------------------------------------------------------
# [baekjoon] 수찾기 (이진탐색, python)
# ----------------------------------------------------------------------------
import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr.sort()
M = int(input())

temp = list(map(int, input().split()))

for i in temp:
    start_idx = 0
    end_idx = N-1
    find = False

    # 이분 탐색
    while start_idx <= end_idx:
        mid = (start_idx + end_idx)//2

        if i > arr[mid]:     # 가운데가 target보다 작으면
            start_idx = mid + 1
        elif i < arr[mid]:
            end_idx = mid - 1
        else:
            find = True
            break
    
    if find:
        print(1)
    else:
        print(0)




