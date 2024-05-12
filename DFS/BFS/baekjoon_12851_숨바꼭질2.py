# ----------------------------------------------------------------------------
# [baekjoon_12851] 숨바꼭질 2 
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

# 수빈이 위치N, 동생 위치 K
n, k = map(int, input().split())
MAX = 10**5
distance = [0] * (MAX+1)
q = deque()
q.append(n)

result = 0
def bfs():
    global result
    while q:
        x = q.popleft()
        # 탈출조건 K에 도달
        if x == k:
            result += 1
            continue

        for nx in (x-1, x+1, x*2):
            # out of range 체크 및 방문하지 않은 곳, 다시 방문할 떄 같은 값이면 방문할 수 있도록 처리
            if 0 <= nx <= MAX and (not distance[nx] or distance[nx] == distance[x]+1):
                distance[nx] = distance[x] + 1
                q.append(nx)

bfs()

print(distance[k])
print(result)

# 요약
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하여라
# 수빈이는 왼쪽 오른쪽 이동x-1, x+1, 순간이동 2*x 2가지 이동이 가능하다.

# 풀이
# bfs 탐색

# 5 -> 10 ->
# 5 -> 4 -> 
# 5 -> 6

# 핵심은 이미 최소시간이 존재한경우에도 result 증가할수 있어야함.