# ----------------------------------------------------------------------------
# D3[swea_5789] 현주의 상자바꾸기
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    n, q = map(int, input().split())

    nums = [0] * (n+1)

    for i in range(1, q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            nums[j]=i

    print(f"#{tc}", end=" ")
    print(*nums[1:])
