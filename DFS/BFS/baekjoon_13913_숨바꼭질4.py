# ----------------------------------------------------------------------------
# [baekjoon_13913] 숨바꼭질4
# ----------------------------------------------------------------------------
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 10**5
distance = [0] * (MAX+1)
arr = [0] * (MAX+1)

q = deque()
q.append(n)

def route(x):
    tmp = []
    node = x
    for _ in range(distance[x]+1):
        tmp.append(node)
        node = arr[node]
    return ' '.join(map(str, tmp[::-1]))

def bfs():
    while q:
        x = q.popleft()
        if x == k:
            print(distance[k])
            print(route(x))
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not distance[nx]:
                distance[nx] = distance[x] + 1
                q.append(nx)
                arr[nx] = x

bfs()