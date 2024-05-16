# ----------------------------------------------------------------------------
# D3[swea_2930] 힙
# ----------------------------------------------------------------------------
import heapq

for tc in range(1, int(input())+1):
    # 수행해야할 연산의 개수
    N = int(input())

    q = []
    result = []
    for _ in range(N):
        inputs = input().split()
        a = int(inputs[0])
        b = int(inputs[1]) if len(inputs) > 1 else 0

        # 삽입(최대 힙이므로 음수로)
        if a == 1:
            heapq.heappush(q, -b)
        elif a == 2:
            if len(q) == 0:
                result.append(-1)
            else:
                result.append(-heapq.heappop(q))

    print(f"#{tc}", end=" ")
    print(" ".join(map(str, result)))



# 요약
# 1 x  x를 힙에 삽입
# 2 힙에 최대값을 출력하고, 삭제, 단 힙에 출력할 값이 없다면 -1 출력
