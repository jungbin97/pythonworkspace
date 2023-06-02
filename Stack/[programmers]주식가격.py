# ----------------------------------------------------------------------------
# [programmers] 주식가격
# ----------------------------------------------------------------------------

# def solution(prices):
#     answer = [0]*len(prices)

#     for i in range(len(prices)):
#         for j in range(i, len(prices)-1):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 break

#         if prices[len(prices)-1] == 1:
#             answer[len(prices)-1] = 0
#     return answer


# ----------------------------------------------------------------------------
# 더 직관적 코드
# range(5, 4)이면 진행하지 않고 루프 탈출
# ----------------------------------------------------------------------------

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

print(solution([1,2,3,2,3]))