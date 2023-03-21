# ----------------------------------------------------
# [programmers] 포켓몬 (hash)
# 1. N//2갯수 계산하기
# 2. nums 중복 제거
# 3. n//2 개수 >= nums 개수면 n//2 갯수 반환
# 4. 그렇지 않으면 nums개수 반환
# ----------------------------------------------------
# def solution(nums):
#     count = len(nums)//2
#     nums = list(set(nums))     #중복 제거
#     answer = 0
    
#     if count <= len(nums):
#         return count
#     else:
#         return len(nums)

#     return answer

# ----------------------------------------------------
#  다른 풀이
# ----------------------------------------------------
def solution(nums):
    return min(len(nums)//2, len(set(nums)))