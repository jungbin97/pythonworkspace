# ----------------------------------------------------------------------------
# [baekjoon_14888] 연산자 끼워넣기
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

max_value = int(-1e9)
min_value = int(1e9)

operator = list(map(int, input().split()))

def calculation(depth, total, plus, minus, muti, division):
    global max_value, min_value
    # 전부 0이면 탈출
    if depth == N:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return

    if plus:
        calculation(depth+1, total+A[depth], plus-1, minus, muti, division)
    if minus:
        calculation(depth+1, total-A[depth], plus, minus-1, muti, division)
    if muti:
        calculation(depth+1, total*A[depth], plus, minus, muti-1, division) 
    if division:
        calculation(depth+1, int(total/A[depth]), plus, minus, muti, division-1)

calculation(1, A[0], operator[0], operator[1], operator[2], operator[3])

print(max_value)
print(min_value)

# 요약
# N개의 수가 주어짐. 주어진 수의 순서는 바꿀수 없다.
# 연산자 우선순위를 무시하고 순서대로 진행된다.

# 연산자는 N-1개 주어짐.(덧셈, 뺼셈, 곱셈, 나눗셈) 
# 단, 나눗셈은 몫만 사용한다. 음수를 양수로 나누면 양수로 바꾼뒤 몫을 계산 후, 그몫음 음수로 바꾼다.
# 식의 결과가 최대인것과 최소인 것을 구하라

# 풀이