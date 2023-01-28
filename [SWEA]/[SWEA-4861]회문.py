T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())        # N 맵정보 N X N, M : 글자 길이
    graph = []
    for i in range(N):
        graph.append(input())     # 이차원 리스트에 저장

    #행 순회
    for i in range(N):
        for j in range(N-M+1):  # N개 중 M 길이의 회문 판별하기위해 횟수 
            if graph[i][j:j+M] == graph[i][j:j+M][::-1]:
                print("#{} {}".format(test_case, graph[i][j:j+M]))

    #열 순회
    for i in range(N-M+1):  # N개 중 M 길이의 회문 판별하기위해 횟수
        for j in range(N):
            tmp = []
            for k in range(M):
                tmp.append(graph[k+i][j])
            if tmp == tmp[::-1]:    # 회문인경우 
                print("#{} {}".format(test_case, ''.join(tmp)))
            