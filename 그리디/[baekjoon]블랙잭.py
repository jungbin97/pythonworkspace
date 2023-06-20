# ----------------------------------------------------------------------------
# [baekjoon] 블랙잭(그리디, python)
# ----------------------------------------------------------------------------
from itertools import combinations
result = 0
n, m = map(int, input().split())
cards = list(map(int, input().split()))

card_comb = list(combinations(cards, 3))

for i in card_comb:
    temp = sum(i)
    if result < temp <= m:
        result = temp
        

print(result)
# ----------------------------------------------------------------------------
# pass
# ----------------------------------------------------------------------------

# from itertools import combinations
# result = []
# n, m = map(int, input().split())
# cards = list(map(int, input().split()))

# card_comb = list(combinations(cards, 3))

# for i in card_comb:
#     if sum(i) > m:
#         continue
#     else:
#         result.append(sum(i))
        

# print(max(result))
# ----------------------------------------------------------------------------
# 반복문 사용(완전 탐색)
# ----------------------------------------------------------------------------
n, m = map(int, input().split())
cards = list(int, input().split())
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                result = max(result, cards[i]+cards[j]+cards[k])

print(result)