# ----------------------------------------------------------------------------
# [programmers] 단어변환
# 최소 단계 즉 최단 경로를 구해야하므로 (BFS)
# ----------------------------------------------------------------------------
from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])    # [단어, 깊이]
    V = [0] * (len(words))  # 방문 노드 여부 확인 리스트

    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            # 만약 확인 안한 단어 이면
            if not V[i]:
                # 그 단어가 words속 단어와 다를떄 한자씩 비교해서 더하기
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1

                if temp_cnt == 1:   # 만약 다른 글자 개수가 1개라면
                    q.append([words[i], cnt+1])
                    V[i] = 1
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))