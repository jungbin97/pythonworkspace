# ----------------------------------------------------------------------------
# [programmers] 전화번호목록
#  1. startswith를 사용해 문자열이 서로 접두어인지 확인한다.
# ["6", "12", "6789"] 일때 6 -> 1, 12 -> 6 
# ----------------------------------------------------------------------------
# def solution(phone_book):
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i].startswith(phone_book[j]):
#                 return False
#             if phone_book[j].startswith(phone_book[i]):
#                 return False
#     return True


# print(solution(["6", "12", "6789"]))
# ----------------------------------------------------------------------------
# 정렬을 통해 비교한 연산을 줄여준다.
# ["12", "6", "6789"]이라면
# 1. 정렬을 오름차순으로 해주었으므로 12 -> 6 이다르면 12와 6이후에 것들은 어짜피 다르기떄문에
# 비교해줄 필요가 없다.
# 2. 또한 양방향으로 6 -> 12가 같은지 확인 할 필요가 없다.
# ----------------------------------------------------------------------------
# def solution(phone_book):
#     # 전화번호 sorting
#     phone_book.sort()

#     # sorting 한 전화번호부를 2개씩 확인해서 접두어인지 확인
#     for i in range(len(phone_book)-1):
#         if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
#             return False
#     return True

# print(solution(["6789", "68"]))
# ----------------------------------------------------------------------------
# 해시 사용
# value == 1 숫자가 1개 존자한다는 의미
# 각 문자의 서브스트링을 뽑아 문자열 해쉬값이 같은 것이 hashMap에 존재한다면 false를 반환
# ----------------------------------------------------------------------------
def solution(phone_book):
    # Hash map을 만든다
    hashMap = {}
    for i in phone_book:
        hashMap[i] = 1

    # 접두어가 Hash map에 존재하는 찾는다.
    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num

            # 본인 자체일 경우는 제외
            if arr in hashMap and arr != nums:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))