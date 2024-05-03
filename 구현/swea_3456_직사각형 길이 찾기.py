# ----------------------------------------------------------------------------
# [baekjoon_3456] 직사각형 길이 찾기 
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    arr_set = set(arr)
    
    if len(arr_set) == 2:
        total = sum(arr_set) * 2
    elif len(arr_set) == 1:
        total = sum(arr_set) * 4

    result = total - sum(arr)
    print(f"#{tc} {result}")


# 풀이
# 중복 제거 후 직사각형 둘레 구하기 - 현재 값 = 나머지 직사각형 변 길이