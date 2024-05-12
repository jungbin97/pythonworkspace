# ----------------------------------------------------------------------------
# [baekjoon_13549] 숨바꼭질3
# ----------------------------------------------------------------------------
from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
MAX = 10**5
distance = [0] * (MAX+1)


q = deque()
if n == 0:
    q.append(1)
else:
    q.append(n)
    
def bfs():
    while q:
        x = q.popleft()

        if x == k:
            return distance[k]

        for nx in (x-1, x+1, x*2):
            if 0<= nx <= MAX and not distance[nx]:
                # 순간이동하면
                if nx == x*2:
                    distance[nx] = distance[x]
                    q.appendleft(nx)
                else:
                    distance[nx] = distance[x]+1       
                    q.append(nx)

if n == 0:
    if k == 0:
        print(0)
    else:
        print(bfs()+1)
else:
    print(bfs())