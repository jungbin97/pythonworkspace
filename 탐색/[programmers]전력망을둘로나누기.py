# ----------------------------------------------------------------------------
# [programmers] 전력망을 둘로 나누기 (완전탐색, BFS)
# 연결된 간선을 모두 끊어 BFS로 노드 개수 카운트
# 시간 복잡도 : O(N^2)
# ----------------------------------------------------------------------------
from collections import deque

def solution(n, wires):
    answer = 0
    
    # 간선정보 그래프로 초기화
    graph = [[] for _ in range(n+1)]
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)
        
    def BFS(start):
        visited = [0] * (n + 1)
        q = deque([start])
        visited[start] = 1
        cnt = 1

        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    # 해당 노드 방문처리
                    visited[i] = 1
                    cnt += 1
        return cnt
    
    answer = n
    for a,b in wires:       # 모든 간선 루프, 시간 복잡도 : O(n-1)
        # 그래프 연결 끊기
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 노드 개수 차이
        answer = min(abs(BFS(a) - BFS(b)), answer)  # 각 노드와 간선 한번씩 방문 O(n + (n-1))

        # 다음 연결확인을위해 연결 복구
        graph[a].append(b)
        graph[b].append(a)
        
    return answer

n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
print(solution(n, wires))
