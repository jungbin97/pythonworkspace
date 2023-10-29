def solution(n):
    arr = [[0] * n for _ in range(n)]
    result = []

    # 방향을 선택할 조건을 찾아야함.
    x, y = -1, 0
    cnt = 1

    for i in range(n):
        for j in range(i, n):
            # 아래
            if i % 3 == 0:
                x += 1
                
            # 오른쪽
            if i % 3 == 1:
                y += 1
            
            # 위쪽
            if i % 3 == 2:
                x -= 1
                y -= 1
            
            arr[x][y] = cnt
            cnt += 1
            

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                break
            result.append(arr[i][j])

    return result



print(solution(4))
