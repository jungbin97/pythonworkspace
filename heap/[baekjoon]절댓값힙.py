# ----------------------------------------------------------------------------
# [baekjoon-11286] 절댓값힙(heap, python)
# ----------------------------------------------------------------------------
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
h = []
result = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if len(h)>0:
            print(heapq.heappop(h)[1])    # 가장 작은 값 출력
        else:
            print(0)
    else:
        heapq.heappush(h, ((abs(num), num)))
