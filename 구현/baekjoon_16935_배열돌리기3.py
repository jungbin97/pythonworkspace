# ----------------------------------------------------------------------------
# [baekjoon_16935] 배열돌리기3 
# ----------------------------------------------------------------------------
from copy import deepcopy

# 행, 열, 연산 수R
n, m, r = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]

def rotation(A, num):
    # 행열의 개수가 바뀔수도 있으니 갱신해야함.
    n = len(A)
    m = len(A[0])
    # 1번연산(상하 반전)
    if num == 1:
        return A[::-1]
   # 2번연산(좌우 반전)
    elif num == 2:
        new_A = []
        for tmp in A:
            new_A.append(list(tmp[::-1]))
        return new_A

    # 3번연산(오른쪽으로 90도)
    elif num == 3:
        new_A = []
        for tmp in list(zip(*A)):
            new_A.append(list(tmp[::-1]))
        return new_A

    # 4번연산(왼쪽으로 90도)
    elif num == 4:
        return list(map(list, zip(*A)))[::-1]
    
    elif num == 5:
        new_A = deepcopy(A)
        for i in range(n//2):
            for j in range(m//2):
                new_A[i][j+m//2] = A[i][j]
                new_A[i+n//2][j+m//2] = A[i][j+m//2]
                new_A[i+n//2][j] = A[i+n//2][j+m//2]
                new_A[i][j] = A[i+n//2][j]
        return new_A
        
    elif num == 6:
        new_A = deepcopy(A)
        for i in range(n//2):
            for j in range(m//2):
                new_A[i+n//2][j] = A[i][j]
                new_A[i+n//2][j+m//2] = A[i+n//2][j]
                new_A[i][j+m//2] = A[i+n//2][j+m//2]
                new_A[i][j] = A[i][j+m//2]
        return new_A


# 연산 번호
num = list(map(int, input().split()))
for i in range(r):
    A = rotation(A, num[i])

for row in A:
    print(" ".join(map(str, row)))