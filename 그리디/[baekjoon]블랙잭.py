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