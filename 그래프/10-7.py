# ----------------------------------------------------------------------------
# [이코테] 팀 결성 (그래프, python)
# ----------------------------------------------------------------------------
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# n : 0~n번까지 팀 번호 (총n+1개), m : 연산 개수
n, m = map(int, input().split())
parent = [0] * (n+1)    # 부모 테이블 

# 부모 테이블, 부모를 자기자신으로 초기화 값 세팅
for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합(union) 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")