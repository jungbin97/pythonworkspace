# ----------------------------------------------------------------------------
# [programmers] 여행 경로
# ----------------------------------------------------------------------------
def solution(tickets):
    answer = []
    goal = len(tickets) + 1
    # 방문 체크
    visited = [False] * len(tickets)

    def dfs(airport, path):
        # 탈출조건
        if len(path) == goal:
            answer.append(path)
            return
        
        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])

    # 방문순서를 알파벳 순으로 정렬하여 빠른것을 선택
    answer.sort()

    return answer[0]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))