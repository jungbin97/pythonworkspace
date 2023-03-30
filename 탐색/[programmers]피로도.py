# ----------------------------------------------------------------------------
# [programmers] 피로도 (완전탐색)
#  1. 모든 경우의 수 고려 permutaions (순열 - 순서고려)
#  2. 현재피로도(k)가 최소피로도와 같거나 크면
#  3. 던전 방문(+1) 소모 피로도 만큼 감소시킴
#  4. 탐험 할 수 있는 최대 던전 수 출력 
# ----------------------------------------------------------------------------
from itertools import permutations

def solution(k, dungeons):
    cnt = 0
    l = len(dungeons)
    for i in permutations(range(l)):
        tmp_k = k
        for idx, value in enumerate(i):
            if tmp_k >= dungeons[value][0]:     # 최소피로도 보다 크거나 같으면
                cnt = max(cnt, idx+1)       # 가장 많이 방문한 던전 갱신
                tmp_k -= dungeons[value][1]     # 소모피로도 만큼 감소
            else:
                break
    return cnt
        

print(solution(80, [[80,20],[50,40],[30,10]]))