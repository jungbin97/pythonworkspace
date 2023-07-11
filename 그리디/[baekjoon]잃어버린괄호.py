# ----------------------------------------------------------------------------
# [baekjoon] 잃어버린괄호(그리디, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

answer = 0
str = input().rstrip()
arr = str.split("-")

for i in arr[0].split("+"):
    answer += int(i)
for i in arr[1:]:
    for j in i.split("+"):
        answer -= int(j)

print(answer)

