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


# ---------------------------------------------------------------------------
# 더 직관적 코드
# range(5, 4)이면 진행하지 않고 루프 탈출
# 시간 복잡도 : O(N^2)
# ----------------------------------------------------------------------------

# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer

# print(solution([1,2,3,2,3]))
# ---------------------------------------------------------------------------
# stack 이용한 풀이
# 가격이 떨어진 것이 있는 것 먼저 처리(pop)
# stack에 남아있는 것은 가격이 떨어진지 않은 것들이다. 하나씩 꺼내서 처리
# 시간 복잡도 :O(N)
# ---------------------------------------------------------------------------

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            pastIdx, price = stack.pop()
            answer[pastIdx] = i - pastIdx

        stack.append([i, prices[i]])

    for i, _ in stack:
        answer[i] = len(prices) - i - 1
    
    return answer


print(solution([1,2,3,2,3]))