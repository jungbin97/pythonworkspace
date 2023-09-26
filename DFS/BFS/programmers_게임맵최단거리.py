# ----------------------------------------------------------------------------
# [programmers] 게입 맵 최단거리 (bfs, python) 
# ----------------------------------------------------------------------------
from collections import deque

def solution(maps):
    def bfs(x, y):
        
        while q:
            # 큐에서 뺴기
            x, y = q.popleft()

            # 탈출 조건(도착 위치 도달)
            if (x == n-1) and (y == m-1):
                return visited[x][y]

            # 상하 좌우 이동
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx = x+dx
                ny = y+dy
                
                # 인덱스 범위 쳌크
                if (nx >= 0 and ny >=0 and nx < n and ny < m):
                    if (maps[nx][ny] == 1 and visited[nx][ny] == 0):
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
        return -1


        
    m = len(maps[0])
    n = len(maps)
    
    # 방문 처리 리스트 초기화(거리 카운트로도 사용)
    visited = [[0]*m for _ in range(n)]

    # 처음 위치 방문처리
    q = deque([(0,0)])
    visited[0][0] = 1
    
    return bfs(0, 0);