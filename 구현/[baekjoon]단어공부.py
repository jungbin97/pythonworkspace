# ----------------------------------------------------------------------------
# [baekjoon] 단어공부(구현, python)
# rstrip()으로 개행문자르 제거해야 문자 하나 들어왔을때 제대로 출력됨
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline
str=input().rstrip().upper()

str_set = list(set(str))
result = []

for x in str_set:
    result.append(str.count(x))
    
# count 숫자가 여러개면 최댓값이 중복 된다는 뜻
if result.count(max(result)) > 1:
    print("?")
else:
    print(str_set[result.index(max(result))])