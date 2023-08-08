# ----------------------------------------------------------------------------
# [baekjoon-2606] 바이러스(dfs, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

def dfs(i):
    global cnt
    visited[i] = 1
    for j in graph[i]:
        if visited[j]==0:
            dfs(j)
            cnt += 1

# 컴퓨터 수
n = int(input())
# 연결 간선 개수
m = int(input())

graph = [[0] for _ in  range(n+1)]
visited = [0]*(n+1)
cnt = 0

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)  # 양 방향 연결
    graph[b].append(a)
dfs(1)

print(cnt-1)