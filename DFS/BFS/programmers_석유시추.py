# ----------------------------------------------------------------------------
# [programmers] 석유 시추
# ----------------------------------------------------------------------------
from collections import deque

def solution(land):
    # 세로(행), 가로(열)
    n, m = len(land), len(land[0])
    
    # 방문체크 배열
    visited = [[False]*(m) for _ in range(n)]
    
    # 이동방향(상하좌우)
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    max_oil_col = [0] * m
    
    def bfs(x, y):
        q = deque([(x, y)])
        # 방문처리
        visited[x][y] = True
        count = 1
        # 현재 석유덩어리에서 최소열, 최대열 찾기
        min_y, max_y = y, y
        
        # bfs 탐색
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx = dx + x
                ny = dy + y
                # 범위체크, 방문했는지, 석유인지
                if 0<= nx <n and 0 <= ny <m and not visited[nx][ny] and land[nx][ny] == 1:
                    count += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    min_y = min(min_y, ny)
                    max_y = max(max_y, ny)
        
        # 해당 석유 덩어리의 최소 열부터 최대열 까지, 반환한 크기 누적합해주기
        for y in range(min_y, max_y+1):
            max_oil_col[y] += count
                    
    # 열 탐색
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                
    return max(max_oil_col)
        

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))


# 요약
# 석유시추관은 단하나, 열을 관통할 수 있다.
# 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있음.
# 시추관 하나를 설치해 가장 많은 석유랑을 return 하도록 해라.

# 풀이 
# 열을 하나씩 골라 1이있으면 bfs로 전부탐색하여 총 개수 고름
# 총 개수를 비교하여 최대값을 반환

# 최적화
# bfs을 덩어리 별로 한번씩만 하도록 제한한다.(이전 코드는 열을 이동할떄마다 해당하는 덩어리 bfs 탐색함.)
# 덩어리의 최소열, 최대열을 구해서 그사이의 해당하는 열은 덩어리 크기를 누적해준다.
# 크기 누적한 열의 일차원 배열에서 가장 큰값을 구하는게 최대 시추가능한 열의 석유량이다.