# ----------------------------------------------------------------------------
# [programmers] 프로세스 (Queue, python)
# any() 함수는 list의 원소를 조건 검사 할 때 사용(리스트 길이가 n일때 시간 복잡도 O(n))
# 반환 값은 조건에 만족하면 True, False로 반환
# ----------------------------------------------------------------------------
from collections import deque
def solution(priorities, location):
    q = deque()
    answer = 0
    # 우선순위, 순서 튜플로 큐에 삽입
    for index, value in enumerate(priorities):
        q.append((value, index))

    while True:
        current = q.popleft()
        if any(current[0] < i[0] for i in q):   # 큐에 우선순위가 더 큰것이 있을 때
        # if current[0] < max(q[0] for q in q):   # 런타임 에러(testCase 2, 5, 18)
            q.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer

print(solution([1,1,9,1,1,1], 0))
# ----------------------------------------------------------------------------
# 다른 풀이
# ----------------------------------------------------------------------------
