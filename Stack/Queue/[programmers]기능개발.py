# ----------------------------------------------------------------------------
#  [programmers] 기능개발 (큐)
#  1. 작업일 처리 (남은 작업 진도에서 작업속도는 나눈 몫이 day, 나머지가 있을경우 하루 추가)
#  2. 큐에 peek값을 now에 대입 후 비교해 같거나 작은 것들을 모두 큐에서 뺌
#  3. now보다 큰 작업일을 만날경우 now값 갱신
#  4. 2, 3 과정 반복
# ----------------------------------------------------------------------------
from collections import deque

def solution(progresses, speeds):
    answer = []
    q_day = deque()

    # 작업일 처리
    for i in range(len(progresses)):
        
        day = (100 - progresses[i])//speeds[i]

        # 나머지가 있을 경우 날짜 한번 추가
        if (100 - progresses[i])%speeds[i]:     
            day += 1
        q_day.append(day)

    # q가 빌떄까지 반복    deque peek값 확인
    now = q_day[0]
    count = 0
    while q_day:
        if now >= q_day[0]:
            q_day.popleft()
            count += 1
            if len(q_day) == 0:
                answer.append(count)
        else:
            now = q_day[0]        # now 값 갱신
            answer.append(count)
            count = 0

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))