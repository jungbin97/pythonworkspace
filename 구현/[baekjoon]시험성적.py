# ----------------------------------------------------------------------------
# [baekjoon_9498] 시험 성적(구현, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

grade = int(input().rstrip())

if (90<= grade <= 100):
    print("A")
elif (80<= grade <= 89):
    print("B")
elif (70<= grade <= 79):
    print("C")
elif (60<= grade <= 69):
    print("D")
else:
    print("F")