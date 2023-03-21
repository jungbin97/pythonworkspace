# -------------------------------------------------
# [programmers] 큰수 만들기 (그리디)
# 1. 가장 큰 수를 찾음
# 2. 가장 큰수의 왼쪽 중 가장 작은 수 날림
# 3. k의 개수가 남으면 가장 큰수 오른쪽 가장 작은수 날림
# -------------------------------------------------
def solution(number, k):
    max_value = max(number)     # 아스키 코드로 가장 큰 문자열 반환
    left = []
    right = []
    for i in range(len(number)):    
        if max_value == number[i]:
            left, right = list(number[:i]), list(number[i:])     # 큰 수 기준 왼쪽리스트, 오른쪽 리스트 나눔

    while(k):
        if len(left) != 0:
            left.remove(min(left))
            k -= 1
        else:
            # k가 남고 left가 0이면
            right.remove(min(right))
            k -= 1
    
    answer = "".join(left + right)
    return answer

print(solution("1924", 2))
# ----------------------------------------------------------------
#  테스트 케이스 1 ~ 10 실패 
#  실패요인 : 예제 테스트케이스들만 고려해 알고리즘을 해석(엣지 케이스 고려안함)
#
# ----------------------------------------------------------------