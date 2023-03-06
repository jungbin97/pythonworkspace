# ----------------------------------------
#  [이코테] 두배열의 원소 교체 (정렬)
# ----------------------------------------

# N 배열크기 K 교체 횟수
N, K = map(int, input().split())

# 배열 초기화
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=False) # 오름차순
B.sort(reverse=True) # 내림차순

for i in range(K):
    if A[i] < B[i]:
        # 두원소 교체
        A[i], B[i] = B[i], A[i]
    else:
        break   # A의 원소가 크거나 같을 때 반복문 탈출

print(sum(A))