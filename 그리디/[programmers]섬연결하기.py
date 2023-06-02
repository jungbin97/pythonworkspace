# ----------------------------------------------------------------------------
# [programmers] 섬연결하기 그리디(kruskal)
# 크루스칼 알고리즘 정석 풀이
# ----------------------------------------------------------------------------
def getParent(parent, x):
    if parent[x] != x:
        parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def compareParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return True
    else:
        return False
    

def solution(n, costs):
    answer = 0
    count = 0

    parent = [0] * n    # 노드 개수 만큼 부모노드 테이블 초기화
    for i in range(n):
        parent[i] = i

    # 간선을 비용순으로 정렬
    costs.sort(key = lambda x: x[2])

    for x in costs:
        # 사이클 여부 체크
        if not compareParent(parent, x[0], x[1]):
            answer += x[2]
            unionParent(parent, x[0], x[1])
            count += 1
        
        # 크루스칼 알고리즘은 연결된 간선의 개수가 노드의 개수 -1이기 떄문에
        if count == n-1:
            break

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

# ----------------------------------------------------------------------------
# comapreParent 함수 제거 최적화
# ----------------------------------------------------------------------------
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    # 크루스칼 알고리즘 조건 만족하는지 확인 변수 count
    count = 0

    parent = [0]*n # 노드 개수만큼 부모노드 테이블 초기화
    for i in range(n):
        parent[i] = i

    # 간선을 비용 순서로 정렬
    costs.sort(key = lambda x:x[2])

    for x in costs:
        # 사이클 여부 확인
        if find_parent(parent, x[0]) != find_parent(parent, x[1]):
            union_parent(parent, x[0], x[1])
            answer += x[2]
            count += 1

        # 크루스칼 알고리즘 연결된 간선의 개수는 노드 개수 -1
        if count == n - 1:
            break
    return answer