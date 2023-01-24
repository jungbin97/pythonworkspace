from collections import deque

#N, M을 공백을 구분하여 입력받기
n, m = map(int, input().split())

#2차원 리스트 맵 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

#이동할 상 하 좌 우 방향 정의
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

#BFS 소스 코드 구현
def bfs(x, y):
    #queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    #큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        #미로 찾기 공간 벗어난 경우 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        #괴물이 있는 경우 무시
        if graph[nx][ny] == 0:
            continue
        #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if graph[nx][ny] == 1:
            graph[nx][ny] == graph[x][y] + 1
            queue.append((nx, ny))
            
    
