# ----------------------------------------------------------------------------
# [baekjoon_2814] 최장 로로
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    # 정점, 간선
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    result = 0

    for _ in range(m):
        # a->b , b->a 무방향이므로 둘다 추가
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, cnt):
        global result
        visited[node]  = True

        for i in graph[node]:
            if not visited[i]:
                dfs(i, cnt + 1)
        visited[node]  = False

        if cnt > result:
            result = cnt

    for i in range(1, n+1):
        visited = [False] * (n+1)
        dfs(i, 1)

    print(f"#{tc} {result}")

# 요약
# 가중치가 없는 무방향 그래프에서 최장 경로의 길이를 구하여라(경로는 정점의 개수를 말한다.)
# 방문한 정점은 한번이상 방문 불가, 

# 풀이
# 시작 노드를 모든 노드를 골라 진행.