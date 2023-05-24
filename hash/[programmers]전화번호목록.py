# ----------------------------------------------------------------------------
# [programmers] 전화번호목록
#  1. startswith를 사용해 문자열이 서로 접두어인지 확인한다.
# ["6", "12", "6789"] 일때 6 -> 1, 12 -> 6 
# ----------------------------------------------------------------------------
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True


print(solution(["6", "12", "6789"]))
