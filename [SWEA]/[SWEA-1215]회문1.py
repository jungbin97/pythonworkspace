# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
for test_case in range(1, 11):
    # 찾을 회문의 길이
    length = int(input())

    # 그래프 초기화
    graph = []
    for i in range(8):
        graph.append(input())
    
    result = 0
    # 행 순회
    for i in range(8):
        for j in range(8-length+1): # 한행에 회문 판별하기 위한 횟수
            if graph[i][j:j+length] == graph[i][j:j+length][::-1]:    # 뒤집어서 같으면 회문
                result += 1

    # 열 순회(한열의 모든 회문을 탐색하고 다음열로 넘어가는게 아니라 모든 열을 한번탐색후 다시 돌아옴)
    for i in range(8-length+1):
        for j in range(8):
            tmp = []
            for k in range(length):
                tmp.append(graph[k+i][j])
            if tmp == tmp[::-1]:    # 회문인 경우
                result += 1

    print("#{} {}".format(test_case, result))
