# def solution(citations):
#     answer = 0
#     citations.sort()    # 오름차순 정렬
#     h2 = []

#     for i in range(len(citations)):
#         h2.append(len(citations) - i)
#         if citations[i] == h2[i]:
#             answer = h2[i]
#             return answer
#     return answer

# print(solution([3, 0, 6, 1, 5]))
# ---------------------------------------------------test case 1개 통과 ----------------------------------------------
#  논문 인용횟수 h, 인용횟수가 h이상인 논문의 수 같지 않을 경우를 고려하지 않았다.
#  주어진 테스트케이스만 고려하고 나머지 엣지 케이스를 고려하지 않았기 때문
# -------------------------------------------------------------------------------------------------------------------
def solution(citations):
    citiations = sorted(citations)
    for i in range(len(citations)):
        if citations[i] >= len(citations) - 1:
            return len(citations) - i
    return 0
 
print(solution([3, 0, 6, 1, 5]))
# -------------------------------------------------------------------------------------------------------------------
# min(index,value) 부분은 가능할 수 있는 모든 h-index를 추출하는 부분 
# 2) max(~) 값은 가능할 수 있는 모든 h-index 중 가장 큰 값을 추출하는 부분으로 생각하시면 됩니다. 
# 예를들어 [6, 5, 4, 1, 0]의 경우에선 min~ 부분은 min(1, 6), min(2, 5), min(3, 4), min(4, 1), min(5, 0)
# 즉 해당 인용수 이상의 논문개수와 해당 논문의 인용수 중 더 작은 숫자를 고르는 작업을 하고(h-index로 가능한 숫자 추출)
#  max~부분은 앞에서 골라진 (1, 2, 3, 1, 0) 중 가장 큰 숫자를 뽑아 실제 h-index를 구하는 방법입니다. 
# -------------------------------------------------------------------------------------------------------------------
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer