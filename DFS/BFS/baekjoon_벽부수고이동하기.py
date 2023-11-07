import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

# 방문처리, 벽뿌순지
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
# 상하좌우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    q = deque()
    q.append([0, 0, 0])
# 방문 처리
    visited[0][0][0] = 1
    

    while q:
        x, y, wall = q.popleft()
        
        # 탈출 조건
        if x == N-1 and y==M-1:
            return visited[x][y][wall]

        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            # 맵 인덱스 체크, 방문 체크(방문하지 않은 곳)
            if 0<= nx < N and 0<= ny < M:
                # 벽이 아니고 한번도 방문하지 않은 경우
                if arr[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    q.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[x][y][wall] + 1

                # 한번도 부수지 않고 벽이면
                if wall == 0 and arr[nx][ny] == 1:
                    # 벽을 부순 상태로
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][0] + 1
    
    return -1

print(bfs())