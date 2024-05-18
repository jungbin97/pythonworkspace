# ----------------------------------------------------------------------------
# D3[swea_13428] 숫자 조작
# ----------------------------------------------------------------------------
def swap(i, j, string):
    s_list = list(string)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    number = "".join(s_list)
    return number
for tc in range(1, int(input())+1):
    N = input()
    result_min = int(N)
    result_max = int(N)

    for i in range(len(N)-1):
        for j in range(i, len(N)):
            number = swap(i, j, N)
            if number[0] == "0":
                continue
            if int(number) > result_max:
                result_max = int(number)
            if int(number) < result_min:
                result_min = int(number)

    print(f"#{tc} {result_min} {result_max}")


# 요약
# 9자리 이하의 음이 아닌 정수 N이 주어짐
# 한쌍의 숫자를 골라 위치를 위치를 최대 한번 바꿔(안바꾸거나, 바꾸거나)새로운 수를 M을 만든다.(단 바꾼결과가 맨앞에 0이면 안됨)
# M의 최솟값과 최댓값을 구하여라

# 조합을 완탐 돌림
# 단, 맨앞이 0인경우는 제외