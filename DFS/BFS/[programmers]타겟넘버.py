# count = 0
# def dfs(idx, value, numbers, target):
#     global count

#     length = len(numbers)
#     if (idx == length and target == value):
#         count += 1
#         return
#
#     if(idx == length):
#         return
#     dfs(idx+1, value+numbers[idx], numbers, target)
#     dfs(idx+1, value-numbers[idx], numbers, target)

# def solution(numbers, target):
#     global count
#     dfs(0, 0, numbers, target)
#     return count
# ---------------------------------------------------------------
#  DFS 풀이 
# ---------------------------------------------------------------
from itertools import product
def solution(numbers, target):
    l  = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
# ---------------------------------------------------------------
# ex) l = [4, 1, 2, 1] 
#     l = [(4, -4), (1, -1), (2, -2), (1, -1)] 
#     product(*l) => (4,1,2,1), (4,1,2,-1), ...
#     리스트 내의 모든 경우의 수 데카르트 곱
# ---------------------------------------------------------------