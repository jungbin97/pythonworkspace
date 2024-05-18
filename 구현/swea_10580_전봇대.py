# ----------------------------------------------------------------------------
# D3[swea_10580] 전봇대
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    # 전선 개수
    N = int(input())

    wire = []
    for _ in range(N):
        a, b = map(int, input().split())
        wire.append((a,b))

    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (wire[i][0] < wire[j][0] and wire[i][1] < wire[j][1]) or (wire[i][0] > wire[j][0] and wire[i][1] > wire[j][1]):
                continue
            result += 1

    print(f"#{tc} {result}")

# 요약
# 전봇대의 교차점을 찾아라

# 풀이
# 교차점은 등호가 다르면 생김.
# (a1, b1), (a2, b2) 두개 의 전선이 있다면
# (a1 > a2 and b1 > b2) (a1 < a2 and b1 < b2) 이것만 아니면 교차점은 생긴다.