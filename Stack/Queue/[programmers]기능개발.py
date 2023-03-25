# ----------------------------------------------------------------------------
#  [programmers] 기능개발 (큐)
#  1. 작업일 처리 (남은 작업 진도에서 작업속도는 나눈 몫이 day, 나머지가 있을경우 하루 추가)
#  2. 큐에 peek값을 now에 대입 후 비교해 같거나 작은 것들을 모두 큐에서 뺌
#  3. now보다 큰 작업일을 만날경우 now값 갱신
#  4. 2, 3 과정 반복
# ----------------------------------------------------------------------------

# from collections import deque

# def solution(progresses, speeds):
#     answer = []
#     q_day = deque()

#     # 작업일 처리
#     for i in range(len(progresses)):
        
#         day = (100 - progresses[i])//speeds[i]

#         # 나머지가 있을 경우 날짜 한번 추가
#         if (100 - progresses[i])%speeds[i]:     
#             day += 1
#         q_day.append(day)

#     # q가 빌떄까지 반복    deque peek값 확인
#     now = q_day[0]
#     count = 0
#     while q_day:
#         if now >= q_day[0]:
#             q_day.popleft()
#             count += 1
#             if len(q_day) == 0:
#                 answer.append(count)
#         else:
#             now = q_day[0]        # now 값 갱신
#             answer.append(count)
#             count = 0

#     return answer

# print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))

# ----------------------------------------------------------------------------
# 작업일 처리 개선(Math.ceil 사용) -> 나머지가 있으면 무조건 올림처리
# ----------------------------------------------------------------------------
# from collections import deque
# import math

# def solution(progresses, speeds):
#     answer = []
#     q_day = deque()

#     # 작업일 처리
#     for i in range(len(progresses)):
#         day = math.ceil((100 - progresses[i])/speeds[i])
#         q_day.append(day)

#     # q가 빌떄까지 반복    deque peek값 확인
#     now = q_day[0]
#     count = 0
#     while q_day:
#         if now >= q_day[0]:
#             q_day.popleft()
#             count += 1
#             if len(q_day) == 0:
#                 answer.append(count)
#         else:
#             now = q_day[0]        # now 값 갱신
#             answer.append(count)
#             count = 0

#     return answer

# print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))

# ----------------------------------------------------------------------------
# zip() 함수 -> 튜플 형태로 반환
# zip() 함수 사용이유 : 작업일을 처리할때 동일한 인덱스를 사용하므로 합쳐서 계산이 쉽도록 함

# -(p-100)//s 부분 Math.ceil 없이 처리하기 위함
# (p-100) => 음수
# (p-100) // s => 내림한 음수(음수에서 내림은 절대값은 커짐)
# -((p-100)//s) => 올림한 양수
# ----------------------------------------------------------------------------
def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]

print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))