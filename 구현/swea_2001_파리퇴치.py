# ----------------------------------------------------------------------------
# D2[SWEA_2001] 파리 퇴치
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    # 루프
    for i in range((n-m)+1):
        for j in range((n-m)+1):
            tmp = 0
            for k in range(i, i+m):
                for l in range(j, j+m):
                    tmp += graph[k][l]
            result = max(result, tmp)

    print("#{} {}".format(tc, result))

# 요약
# N X N 배열 안의 숫자는 해당 영역안에 존재하는 파리의 개수이다.
# M X M 크기의 파리채를 한번 내리쳐서 최대의 파리를 죽이고자 한다.
# 최대 죽은 파리수를 구하여라.

# 풀이
# 루프는 (n-m+1)