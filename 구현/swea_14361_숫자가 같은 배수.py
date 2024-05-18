# ----------------------------------------------------------------------------
# D3[swea_14361] 숫자가 같은 배수
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    N = input()
    N_sort = sorted(list(N))

    flag = False
    k = 2 #2의 배수로 시작
    while True:
        # 2 * k, 3 * k
        multi_num = int(N) * k
        # 문자열 길이가 더크면(탈출조건)
        if len(str(multi_num)) > len(N):
            break

        # 정렬된 값이 같으면 같은 숫자로 배수로 만든것.
        if sorted(list(str(multi_num))) == N_sort:
            flag = True
            break
        k += 1

    if flag:
        result = "possible"
    else:
        result = "impossible"

    print(f"#{tc} {result}")

# 요약
# 숫자 N을 재배열 해서 N보다 큰 N의 배수를 만들 수 있는지 판단한 프로그램을 작성


# 풀이
# N의 배수를 탐색, 배수의 길이가 N보다 길면 안됨(탈출조건)
# 정렬된 값이 같으면 같은 숫자로 배수 만든것으로 간주