# ----------------------------------------------------------------------------
# D2[swea_1970] 쉬운 거스름돈
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    N = int(input())

    coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0] * len(coins)
    for i in range(len(coins)):
        if N >= coins[i]:
            result[i] = N//coins[i]
            N = N%coins[i]
    print(f"#{tc}")
    print(" ".join(map(str, result)))