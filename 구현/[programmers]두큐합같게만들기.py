# -----------------------------------------------
# 반복문 탈출조건을 찾는것이 상당히 까다로움
# queue1에서 전부 빼서 queue2에 추가하고 queue2에서 전부 빼고 queue1에 추가되면 모든 원소를 바꾼것 => len(q1)X2
# 다시 원래 모습으로 바꾸려면 => len(q1) X4 만큼 횟수필요

# 하지만 len(q1) X 3 도가능
# 반례로 테스트케이스 q1=[1, 1, 1, 8, 10, 9] q2= [1, 1, 1, 1, 1, 1]가 여기에 해당
# 총 14회 이동하면 합이 같아짐
# len(q1) X 3 = 18이므로 통과 가능! 
# 횟수를 더 타이트하게 하려면 len(q1)*3 - 3도 통과
# -----------------------------------------------
from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1, sum2 = sum(q1), sum(q2)
    
    escape_cnt = len(q1) * 4

    while escape_cnt:
        escape_cnt -= 1
        # if answer > escape_cnt:
        #     return -1
        
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())
        elif sum1 < sum2:
            sum2 -= q2[0]
            sum1 += q2[0]
            q1.append(q2.popleft())
        if escape_cnt == 0:
            return answer

        answer += 1
        print(q1, end=" ")
        print(q2)

print(solution([1, 1, 1, 8, 10, 9], [1, 1, 1, 1, 1, 1]))
