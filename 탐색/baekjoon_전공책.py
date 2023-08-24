# ----------------------------------------------------------------------------
# [baekjoon_16508] 전공책 (DFS, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

min_val = int(1e9)
# 만들고자 하는 단어
T = input().strip()

# 전공책 개수
N = int(input().rstrip())

books = []
costs = []

# 대문자 알파벳 총 26가지
select_cnt = [0]*26
cnt = [0]*26

for i in range(len(T)):
    cnt[ord(T[i])-65] += 1

# 입력
for _ in range(N):
    cost, book = map(str, input().split())
    costs.append(int(cost))
    books.append(book)

# 체크하는 부분 cnt[i]가 더크다면 단어를 만들수 없다
def check():
    for i in range(len(cnt)):
        if cnt[i] > select_cnt[i]:
            return False
    return True

def dfs(idx, total):
    global min_val
    if idx == N:
        if check():
            min_val = min(min_val, total)
        return
    
    for i in range(len(books[idx])):
        select_cnt[ord(books[idx][i])-65] += 1
    dfs(idx+1, total+costs[idx])

    for i in range(len(books[idx])):
        select_cnt[ord(books[idx][i])-65] -= 1
    dfs(idx+1, total)

dfs(0,0)

print(-1 if min_val == int(1e9) else min_val)