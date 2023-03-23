# -------------------------------------------------
# [programmers] 큰수 만들기 (그리디)
# 1. 가장 큰 수를 찾음
# 2. 가장 큰수의 왼쪽 중 가장 작은 수 날림
# 3. k의 개수가 남으면 가장 큰수 오른쪽 가장 작은수 날림
# -------------------------------------------------
# def solution(number, k):
#     max_value = max(number)     # 아스키 코드로 가장 큰 문자열 반환
#     # for i in number[::-1]:
#     #     if i > max_value:
#     #         max_value = i

#     left = []
#     right = []
#     for i in range(len(number)):    
#         if max_value == number[i]:
#             left, right = list(number[:i]), list(number[i:])     # 큰 수 기준 왼쪽리스트, 오른쪽 리스트 나눔
#             break       # 첫번째로 큰수만나면 탈출
#     while(k):
#         if len(left) != 0:
#             left.remove(min(left))
#             k -= 1
#         else:
#             # k가 남고 left가 0이면
#             right.remove(min(right))
#             k -= 1
    
#     answer = "".join(left + right)
#     return answer

# print(solution("01010", 3))
# ----------------------------------------------------------------
#  테스트 케이스 2 ~ 10 실패
#  실패요인 : 예제 테스트케이스들만 고려해 알고리즘을 해석
# ----------------------------------------------------------------
def solution(number, k):
    answer = []     # stack

    for i in number:
        if len(answer) == 0:
            answer.append(i)
            continue
        if k>0:
            while answer[-1] < i:
                answer.pop()
                k -= 1
                if len(answer) == 0 or k <= 0:
                    break
        answer.append(i)

    if k > 0:               # "4321" 앞의 숫자가 뒤의 숫자 보다 모두 큰 경우(뒤부터 k개수 삭제)
        answer = answer[:-k] 
    else:
        answer
    
    return ''.join(answer)

print(solution("928857066163493066555730841879", 7))