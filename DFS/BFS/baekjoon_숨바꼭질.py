# ----------------------------------------------------------------------------
# [baekjoon-1697] 숨바꼭질
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

N, K  = map(int, input().split())

dist = [0] * (MAX+1)

q = deque()
q.append(N)
while q:
    X = q.popleft()

    # 탈출 조건
    if X == K:
        print(dist[X])
        break
    for nx in (X-1, X+1, X*2):
        if 0<= nx <= MAX and not dist[nx]:
            dist[nx]= dist[X] + 1
            q.append(nx)







# N은 수빈이 위치, K는 동생 위치
# 수빈 : 걷거나 순간이동 가능,
# 걷기 => 위치가 X일때 1초에 X-1, X+1로 이동 가능
# 순간이동 => 위치가 X일때 1초에 2*X

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지

# 수빈이는 동생의 위치에 가장 근접해야함. UP, DOWN 게임과 유사

# 갈수 있는 경로 (3가지 - 순간이동[X2], 왼쪽이동[-1], 오른쪽이동[1])
# 큐에 삽입
# 큐에 삽입 후 마찬가지로 (3가지 경로 이동)
# 해당 경로가 나오면 종료