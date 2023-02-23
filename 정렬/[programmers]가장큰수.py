# ---------------------------------------------------
#  순열을 위해 완전 탐색으로 해결 해보기
# ---------------------------------------------------

# from itertools import permutations
# def solution(numbers):
#     answer = []
#     arr = list(permutations(numbers, len(numbers)))
#     for i in arr:
#         i = list(map(str, i))
#         i = ''.join(i)  # 구분자가 없으므므로 이어 붙여짐 
#         answer.append(int(i))

#     answer = list(set(answer))
#     answer.sort()
#     return str(answer[-1])

# numbers = [3, 30, 34, 5, 9]
# print(solution(numbers))

# ---------------------------------------------------

# def solution(numbers):
#     input_list = list(map(str, numbers))

#     input_list.sort(key = lambda x:x*3, reverse=True)
    
#     answer = ''
#     answer = answer.join(input_list)
#     return str(int(answer))

# numbers = [3, 30, 34, 5, 9]
# print(solution(numbers))

# ------------ map을 list로 변환해야함.-------------
#  list타입으로 변환하고 변수 저장해야 리스트를 다룰수 있음
#  타입변환없을시 class "map"이 됨
# ------------------------------------------------- 


# ------------------------------------------------- 
#  다른사람 풀이
#   cmp_to_key 사용하는 방법?? => 내부 동작원리를 모르겠음
# ------------------------------------------------- 
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))