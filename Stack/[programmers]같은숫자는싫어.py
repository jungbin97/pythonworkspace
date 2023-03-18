# ---------------------------------------------------
# [programmers] 같은 숫자는 싫어 (Stack/Queue)
# 1. 중복제거
# 2. 순서유지
# ---------------------------------------------------

# def solution(arr):
#     stack = []
    
#     stack.append(arr[0])
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i-1]:
#             stack.append(arr[i])
        
#     return stack

# print(solution([1,1,3,3,0,1,1]))

# ---------------------------------------------------
#  다른 사람 문제 풀이
# ---------------------------------------------------

# def solution(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue      # 리스트 인덱싱 반환값이 리스트이기 때문에
#         a.append(i)
#     return a

# print(solution([1, 3, 3, 0, 3]))

# ---------------------------------------------------
#  출제자의 의도와 가장 적합한 풀이
# ---------------------------------------------------

def solution(s):
    stack = []

    for i in s:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
    
    return stack

print(solution([1,3,3,0,3]))