# ----------------------------------------------------------------------------
# [baekjoon-2750] 수 정렬하기(python)
# 라이브러리 사용
# ----------------------------------------------------------------------------
# import sys

# N = int(sys.stdin.readline().rstrip())

# arr = list(set(int(sys.stdin.readline().rstrip()) for _ in range(N)))

# arr.sort()

# for i in range(N):
#     print(arr[i])
# ----------------------------------------------------------------------------
# 버블정렬 사용
# ----------------------------------------------------------------------------
import sys

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 버블 정렬
for i in range(len(arr)):
    for j in range(0, N-i-1):
        # 만약 현재의 인덱스의 값이 다음 인덱스의 값보다 큰경우
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(N):
    print(arr[i])