# ----------------------------------------------------------------------------
# D3[baekjoon_6485] 삼성시의 버스 노선
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    N = int(input())

    bus_stop = [0] * 5001

    for _ in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            bus_stop[j] += 1

    P = int(input())

    tmp = []
    for _ in range(P):
        c = int(input())
        tmp.append(bus_stop[c])
    print(f"#{tc}", end=" ")
    print(" ".join(map(str, tmp)))