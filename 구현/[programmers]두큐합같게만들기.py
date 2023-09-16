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
