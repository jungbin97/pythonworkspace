# --------------------------------------------
#  [programmers]네트워크 (dfs/bfs)
#  1. 하나의 노드에서 방문할 수 있느 최대한을 방문하면 하나의 네트워크 생성된다.
#  2. 방문한 노드임을 알기위해 visited 리스트를 사용해 중복 방문하지 않도록 한다.
#  3. 탐색은 한 번 수행시 최대한으로 이루어져야하므로 DFS사용
# --------------------------------------------
# def solution(n, computers):

#     def DFS(i):
#         visited[i] = True
#         for a in range(n):
#             if computers[i][a] and not visited[a]:
#                 DFS(a)


#     answer = 0
#     visited = [False for i in range(n)]

#     for i in range(n):
#         if not visited[i]:
#             DFS(i)
#             answer += 1
#     return answer

# --------------------------------------------
# --------------------------------------------
from collections import deque

def solution(n, computers):

    def BFS(i):
        q = deque()
        q.append(i)

        while q:
            i = q.popleft()
            visited[i] = True
            for a in range(n):
                if computers[i][a] and not visited[a]:
                    q.append(a)

    answer = 0
    visited = [False for i in range(n)]

    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1

    return answer