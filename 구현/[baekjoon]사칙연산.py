# ----------------------------------------------------------------------------
# [baekjoon] 사칙연산(구현, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
