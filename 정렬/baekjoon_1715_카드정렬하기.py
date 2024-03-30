# ----------------------------------------------------------------------------
# [baekjoon_1715] 카드 정렬하기
# ----------------------------------------------------------------------------
# import sys
# input = sys.stdin.readline

# N = int(input())

# cards = [int(input().rstrip()) for _ in range(N)]

# # 오름차순으로 정렬
# cards.sort()
# result = 0
# A = cards[0]

# for i in range(1, N):
#     B = cards[i]
#     card_sum = A + B
#     A = card_sum
#     result += card_sum

# print(result)

import sys
import heapq
input = sys.stdin.readline

N = int(input())

# 힙에 초기 카드 묶을 모두 삽입
heap = []
for i in range(N):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙에 원소가 하나 남을때까지 (마지막 결과 값)
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
    
print(result)

# 문제 핵심 요약
# 정렬된 두 묶음의 숫자카드 A, B를 하나로 만든데 A+B번의 비교가 필요.
# N개의 숫자 카드 묶음의 각각 크기가 주어질떄, 최소 몇번의 비교가 필요한지?


# # 풀이
# 10 + 10 + 20 + 40

# 10 + 10 = 20
# 20 + 20 = 40
# 40 + 40 = 80

# => 20 + 40 + 80 = 140

# 10 + 40 = 50
# 50 + 10 = 60
# 60 + 20 = 80

# => 50 + 60 + 80 = 190

# 초반에 가장 작은 수를 만들어야 한다. 그래야 다음에 더하는 수도 작아짐.
# 더해서 나온수도 가장 작은 것 2개를 더해서 결과를 도출하면된다.