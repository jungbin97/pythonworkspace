# ----------------------------------------------------------------------------
# [baekjoon] 토마토
# 최소 일수 구하기 => BFS
# 1. 3차원 배열을 생성
# 2. BFS로 상하좌우앞뒤 6방향을 확인하며 익지 않은 토마토를 체크 후 +1 해준다(일수 체크)
# 3. 가장 큰값(day)를 출력한다. (1부터 시작하므로 일수는 -1해준다)
# 4. 모든 토마토가 익어있을경우 (모두 1인경우) 0출력, BFS후 익지 않은 토마토가 있을 경우 -1출력
# ----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

# 가로, 세로, 높이
m, n, h = map(int, input().split())
graph = []
q = deque()

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append([i,j,k])
    graph.append(tmp)

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while(q):
    x, y, z = q.popleft()

    for i in range(6):
        a = x + dx[i]
        b = y + dy[i]
        c = z + dz[i]

        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c] == 0:
            q.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1   # day +1


complete = False
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                complete = True
                break
            day = max(day, k)
            
if complete:
    print(-1)
else:
    print(day-1)