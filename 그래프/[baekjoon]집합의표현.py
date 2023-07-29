# ----------------------------------------------------------------------------
# [baekjoon] 집합의 표현 (그래프, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 부모테이블 초기화
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    #인덱스와 값이 같으면 자기자신 반환
    if parent[a] != a:
    # 값ㅇ르 인덱스로 바꾸어 재귀로 대표노드 탐색
        parent[a] = find(parent[a])
    return parent[a]

for i in range(m):
    quest, a, b = map(int, input().split())
    
    if(quest == 0):
        union(a, b)
    else:
        if(find(a) == find(b)):
            print("YES")
        else:
            print("NO")