# ----------------------------------------------------------------------------
# D3[swea_3499] 퍼펙트 셔플
# ----------------------------------------------------------------------------
import math

for tc in range(1, int(input())+1):
    N = int(input())
    card = input().split()

    # first 홀수
    first = card[:math.ceil(N/2)]
    second = card[math.ceil(N/2):]

    tmp = []
    for i in range(len(second)):
        tmp.append(first[i])
        tmp.append(second[i])

    if len(first) > len(second):
        tmp.append(first[-1])

    result = " ".join(tmp)
    print(f"#{tc} {result}")


# 요약
# 퍼팩트 셔플의 결과를 출력하라.
# N이 홀수인경우 먼저 놓는 쪽에 한장이 더들어감.


# 풀이
# 총 카드 개수가 홀수면 홀수, 짝수로 나누고
# 짝수면 짝수 짝수로 반 나눈다.
# 번갈아가면서 리스트에 추가하고, 개수가 홀수 짝수이면 홀수개수인 덱이 더 많으므로 마지막에 하나 더 추가한다.


