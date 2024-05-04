# ----------------------------------------------------------------------------
# [baekjoon_1062] 가르침  
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

# 남극 단어, 가르칠수있는 글자
n, k = map(int, input().split())
# 중복제거로 해당 단어를 읽는데 최소 글자 구함.
words = [set(input().rstrip()) for _ in range(n)]
# 방문 체크
check = [False] * 26
answer = 0
def dfs(idx, cnt):
    global answer
    # 글자 5개는 이미 배움
    if cnt == k-5:
        tmp = 0
        for word in words:
            # 배운 글자로 해당 단어를 읽을 수 있는 지 체크
            is_contain = True
            for c in word:
                # 해당 단어에 배우지 않은 글자가 있는 경우
                if not check[ord(c) - ord("a")]:
                    is_contain = False
                    break
            
            if is_contain:
                tmp += 1
        answer = max(answer, tmp)
        return
    
    for i in range(idx, 26):
        if not check[i]:
            check[i] = True
            dfs(i, cnt + 1)
            check[i] = False

if k < 5:
    print(0)
elif k == 26:
    # 모든 단어 다 배울 수 있음.
    print(n)
else:
    for c in ("a", "n", "t", "i", "c"):
        # 해당 알파벳 방문처리
        check[ord(c)-ord("a")] = True
    dfs(0, 0)
    print(answer)

# 요약
# 선생은 K글자만 가르칠수 있음
# 학생은 K개의 글자로만 이루어진 단어를 읽을 수 있음.
# 어떤 K개의 글자를 가르쳐야 단어를 최대 읽을 수 있을까?

# 남극의 모든 단어는 anta로 시작 tica로 끝남. => 5개는 알아야됨.(a, n, t, i, c)
# 남극의 언어에 단어는 N개 밖에 없다.

# 학생들이 읽을 수 있는 단어 최댓값은?

# 풀이
# a, n, t, i, c
# k가 5개 미만이면 0을 반환한다.
# k가 5개 이상이면 k-5 개수만큼 단어택선택할 수 있음.
# 단어는 anta, tica를 자른 문자만 선택

# 어떻게 나머지 문자들을 고를까?
# dfs?