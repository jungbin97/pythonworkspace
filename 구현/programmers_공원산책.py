def solution(park, routes):
    answer = 0
    graph = []
    
    for p in park:
        graph.append(list(p))
        
    d = {"E" : (0, 1), "W" : (0, -1), "N": (-1, 0), "S": (1, 0)}
    
    r = len(graph)
    c = len(graph[0])
    for i in range(r):
        for j in range(c):
            # 시작
            if graph[i][j] == "S":
                x, y = i, j
                break
    
    for route in routes:
        px, py = x, y
        direction, cnt =route.split(" ")
        cnt = int(cnt)
        # 이동 하기
        dx, dy = d[direction]
        for _ in range(cnt):
            nx = x + dx
            ny = y + dy
            # 범위 체크
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "X":
                x, y = nx, ny
            else:
                x, y = px, py
                break
        

    return [x, y]