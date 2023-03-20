# -------------------------------------------------------------------
#  [programmers] 소수찾기 (완전탐색)
#   1. 순열로 생성될 수 있는 문자열 생성
#   2. 생성된 문자열을 int 형으로 변환 후 중복제거(set)
#   3. 소수 찾기 알고리즘으로 소수 구하기
# -------------------------------------------------------------------

from itertools import permutations

def solution(numbers):
    per = []
    answer = 0
    for i in range(len(numbers)):
        per += permutations(numbers, i+1)       # 순열로 모든 경우의수 생성
    new_nums = [int("".join(p)) for p in per]   # 순열 생성된 튜플 문자열 합치고, int형 변환
    
    for i in set(new_nums):
        if isPrime(i):
            answer += 1

    return answer

# 소수 찾기 알고리즘
def isPrime(new_nums):
    if new_nums < 2:
        return False

    for i in range(2, new_nums):
        if new_nums % i == 0:
            return False
        
    return True

print(solution("17"))