# ----------------------------------------------------------------------------
# [baekjoon_10989] 수 정렬하기3(정렬, python)
# 메모리제한, 시간 제한을 참고 해야함.ㅐ
# 메모리제한이 8MB매우 적음
# 일반적인 sort() 사용불가
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = [0] * 10001

for i in range(n):
    num = int(input().rstrip())
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)

