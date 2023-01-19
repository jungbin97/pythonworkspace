T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())    # 입력 받을 사각형 갯수
    count = 0
    matrix = [[0]*10 for _ in range(10)]
    
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())   # [r1,c1] 왼쪽위 모서리, [r2, c2] 오른쪽 아래 모서리, 색상 color
        
        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                if color == 1:
                    if matrix[j][k] == 2:
                        count += 1
                    else:
                        matrix[j][k] = 1
                elif color == 2:
                    if matrix[j][k] == 1:
                        count += 1
                    else:
                        matrix[j][k] = 2
    
    print("#%d %d" %(test_case, count))
                    

