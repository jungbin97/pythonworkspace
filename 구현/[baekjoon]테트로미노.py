# ----------------------------------------------------------------------------
# [baekjoon_14500] 테크노미노
# ----------------------------------------------------------------------------
def dfs(n, m, a, visit, dr, r, c, cnt, rlt, ans):
    visit[r][c] = 1
    rlt += a[r][c]
    cnt += 1
    if cnt == 4:
        ans[0] = max(ans[0], rlt)
        return
    for d in dr:
        x, y = r + d[0], c + d[1]
        if 0 <= x <= n - 1 and 0 <= y <= m - 1 and not visit[x][y]:
            dfs(n, m, a, visit, dr, x, y, cnt, rlt, ans)
            visit[x][y] = 0


def solution(n, m, a):
    visit = [[0] * m for _ in range(n)]
    dr = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    ans = [0]
    for r in range(n):
        for c in range(m):
            dfs(n, m, a, visit, dr, r, c, 0, 0, ans)
            visit[r][c] = 0
            if 0 <= r + 1 <= n - 1 and 0 <= c + 2 <= m - 1:
                ans[0] = max(ans[0], a[r][c] + a[r][c + 1] + a[r][c + 2] + a[r + 1][c + 1])
            if 0 <= r + 2 <= n - 1 and 0 <= c - 1 <= m - 1:
                ans[0] = max(ans[0], a[r][c] + a[r + 1][c] + a[r + 2][c] + a[r + 1][c - 1])
            if 0 <= r - 1 <= n - 1 and 0 <= c + 2 <= m - 1:
                ans[0] = max(ans[0], a[r][c] + a[r][c + 1] + a[r][c + 2] + a[r - 1][c + 1])
            if 0 <= r - 2 <= n - 1 and 0 <= c + 1 <= m - 1:
                ans[0] = max(ans[0], a[r][c] + a[r - 1][c] + a[r - 2][c] + a[r - 1][c + 1])
    return ans[0]


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, A))