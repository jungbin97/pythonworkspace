# ----------------------------------------------------------------------------
# [baekjoon] 백설공주와 일곱난쟁이 (완전탐색, python)
# ----------------------------------------------------------------------------
# arr=[]
# for i in range(9):
#     arr.append(int(input()))
    
    
# for i in range(9):
#     for j in range(i+1,9):
#         if sum(arr)-arr[i]-arr[j]==100:
#             x,y=i,j
#             break
# arr.pop(x)
# arr.pop(y-1)
# for i in arr:
#     print(i)
    

# ----------------------------------------------------------------------------
# 조합 사용
# ----------------------------------------------------------------------------
# from itertools import combinations

# arr = []
# for i in range(9):
#     arr.append(int(input()))

# sum_num = sum(arr)
# for i in combinations(arr, 2):
#     if sum_num-i[0]-i[1] == 100:
#         arr.remove(i[0])
#         arr.remove(i[1])

# for i in arr:
#     print(i)
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
arr = []
for i in range(9):
    arr.append(int(input()))

def func(arr, men_arr, index):
    if len(men_arr) == 7:
        if sum(men_arr) == 100:
            for i in range(len(men_arr)):
                print(men_arr[i])
        
    if index == 9:
        return
    
    func(arr, men_arr+[arr[index]], index+1)
    func(arr, men_arr, index+1)

    

func(arr, [], 0)
