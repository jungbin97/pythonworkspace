# --------------------------------------------------------------
#  1.카펫의 사이즈 경우의 수 구하기
#  2.가로의 길이와 세로의 길이가 같거나 가로가 더김
#  3.가운데 노란색이 있으려면 가로와 세로가 3이상
#  4. 해당 카펫이 입력으로 주어진 개수만큼 노란색격자가 가운데에 있을 수 있는지 구하기
# --------------------------------------------------------------
def solution(brown, yellow):
    ans = []
    total = brown + yellow
    
    for i in range(1, total+1):
        if (total % i) == 0:
            j = total // i  # i: 가로 j: 세로
            if i >= j:
               if(i-2)*(j-2) == yellow:
                    return[i, j]
    return ans

print(solution(24, 24))

# --------------------------------------------------------------
# import math
# def solution(brown, yellow):
#     h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
#     w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
#     return [w,h]

# print(solution(10, 2))