# ---------------------------------------------------------
#  [이코테] 1로 만들기 (DP bottom - up)
#  a-1, a//2, a//3, a//5중 가장 최소값을 골라 원하는 숫자 까지 도달하면 정답(큰문제를 작은 문제로 나눌 수 있음)
#  그래프에서 중복해서 등장하는 수가 있으므로 메모이제이션 기법 사용가능(작은 문제에서 구한 정답이 그것을 포함하는 큰문제에서도 동일하게 적용)
# ---------------------------------------------------------

# 정수 X 입력 받음
X = int(input())

# DP테이블 초기화
d = [0] * 30001     # X의 입력 조건 0 ~ 30000 이기 때문

for i in range(2, X+1):
    d[i] = d[i-1] + 1   # -1 한 경우

    if i % 2 == 0:  # 2로 나눈 경우와 -1한경우 1을 만드는 최소값 비교
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:  # 위에서의 최소값과 5로 나눈경우 1을 만드는 값 비교
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[X])