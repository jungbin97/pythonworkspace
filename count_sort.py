MAX_NUM =  1000

# A는 입력된 숫자를 저장하는 리스트
A = list(map(int, input().split()))

# N은 입력된 숫자 개수
N = len(A)

# 0으로 초기화된 입력될 AMX_NUM+1 길이의 리스트를 생성
count = [0] * (MAX_NUM + 1)
# countSum은 누적합을 저장하는 배열
countSum = [0] * (MAX_NUM + 1)

# 숫자 등장 횟수 세기
for i in range(0, N):
    count[A[i]] += 1

# 숫자 등장 횟수 누적 합 구하기
countSum[0] = count[0]
for i in range(1, MAX_NUM+1):
    countSum[i] = countSum[i-1] + count[i]

# B는 정렬된 결과를 저장하는 리스트
B = [0]*(N+1)

for i in range(N-1, -1, -1):
    B[countSum[A[i]]] = A[i]
    countSum[A[i]] -= 1

# B를 출력
result = ""
for i in range(1, N+1):
    result += str(B[i]) + " "

print(result)