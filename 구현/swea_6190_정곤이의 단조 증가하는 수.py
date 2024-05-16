# ----------------------------------------------------------------------------
# D3[swea_6190] 정곤이의 단조 증가하는 수
# ----------------------------------------------------------------------------
def check(v):
    s = str(v)
    for i in range(0, len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True


for tc in range(1, int(input())+1):
    n = int(input())
    A = list(map(int, input().split()))

    max_value = -1

    for i in range(n-1):
        for j in range(i+1, n):
            value = A[i] * A[j]
            # 단조 증가 체크
            if max_value < value and check(value):
                max_value = value
    print(f"#{tc} {max_value}")


