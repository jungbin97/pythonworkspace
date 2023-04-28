# ----------------------------------------------------------------------------
# [programmers] 피로도 (완전탐색)
#  1. 모든 경우의 수 고려 permutaions (순열 - 순서고려)
#  2. 현재피로도(k)가 최소피로도와 같거나 크면
#  3. 던전 방문(+1) 소모 피로도 만큼 감소시킴
#  4. 탐험 할 수 있는 최대 던전 수 출력 
# ----------------------------------------------------------------------------
# from itertools import permutations

# def solution(k, dungeons):
#     cnt = 0
#     l = len(dungeons)
#     for i in permutations(range(l)):
#         tmp_k = k
#         for idx, value in enumerate(i):
#             if tmp_k >= dungeons[value][0]:     # 최소피로도 보다 크거나 같으면
#                 cnt = max(cnt, idx+1)       # 가장 많이 방문한 던전 갱신
#                 tmp_k -= dungeons[value][1]     # 소모피로도 만큼 감소
#             else:
#                 break
#     return cnt
        

# print(solution(80, [[80,20],[50,40],[30,10]]))
# ----------------------------------------------------------------------------
# DFS 백트래킹 사용
# ----------------------------------------------------------------------------
# answer = 0

# def DFS(k, cnt, dungeons, check):
#     global answer
#     answer = max(answer, cnt)
#     for i in range(len(dungeons)):
#         if check[i] == 0 and k >= dungeons[i][0]:   # 방문하지 않은 던전, 현재피로도가 현재 방문하기위한 최소피로도 보다 크면
#             check[i] = 1
#             # 이전 노드 다시 back 할때, check 값 0으로 돌림
#             # 현재 피로도의 수도 해당 노드를 방문하기 전으로 돌림
#             DFS(k-dungeons[i][1], cnt+1, dungeons, check)
#             check[i] = 0

# def solution(k, dungeons):
#     global answer
#     check = [0]*len(dungeons)       # 방문 여부 체크

#     # cnt : 탐험한 던전 개수, k : 남은 피로도
#     DFS(k, 0, dungeons, check)      # 방문한 던전의 개수를 0으로 초기화

#     return answer

# print(solution(80, [[80,20],[50,40],[30,10]]))
# ----------------------------------------------------------------------------
# 완전탐색 개선(비교 횟수 개선)
# ----------------------------------------------------------------------------
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    l = len(dungeons)
    for i in permutations(range(l)):
        current_k = k
        cnt = 0
        for t in i:
            require, consum = dungeons[t]
            if current_k >= require:     # 최소피로도 보다 크거나 같으면
                cnt += 1                 # 던전 방문 카운트 +1
                current_k -= consum      # 방문한 던전 소모피로도 만큼 감소
        answer = max(answer, cnt)

    return answer
print(solution(80, [[80,20],[50,40],[30,10]]))