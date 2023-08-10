# ----------------------------------------------------------------------------
# [baekjoon] 두 수 비교하기(구현, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

if a<b:
    print("<")
elif a>b:
    print(">")
else:
    print("==")