# ----------------------------------------------------------------------------
# [programmers] 여행 경로 (DFS 풀이)
# 모든 이동경로를 탐색, 최종 2가지 경로가 나오면 오름차순으로 정렬해서 알파벳이 빠른
# 경로를 선택해서 반환한다.
# ----------------------------------------------------------------------------
# def solution(tickets):
#     answer = []
#     goal = len(tickets) + 1
#     # 티켓 사용 체크
#     visited = [False] * len(tickets)

#     def dfs(airport, path):
#         # 탈출조건
#         if len(path) == goal:
#             answer.append(path)
#             return
        
#         for idx, ticket in enumerate(tickets):
#             if airport == ticket[0] and visited[idx] == False:
#                 visited[idx] = True
#                 dfs(ticket[1], path+[ticket[1]])
#                 visited[idx] = False
                
#     dfs("ICN", ["ICN"])

#     answer.sort()

#     return answer[0]

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# ----------------------------------------------------------------------------
# BFS 풀이
# ----------------------------------------------------------------------------
from collections import deque

def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN", ["ICN"], []))

    while q:
        airport, path, used = q.popleft()

        if len(used) == len(tickets):
            answer.append(path)

        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                q.append((ticket[1], path+[ticket[1]], used+[idx]))

    answer.sort()

    return answer[0]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))