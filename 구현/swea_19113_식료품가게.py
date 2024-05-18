# ----------------------------------------------------------------------------
# D3[swea_19113] 식료품 가게
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    # 상점의 품목 수
    N = int(input())

    num = list(map(int, input().split()))
    discount_list = []
    while num:
        for i in range(len(num)):
            if num[i] % 4 == 0 and int(num[i] * 0.75) in num:
                # 정상가
                a = num[i]
                # 할인가
                b = int(num[i] * 0.75)

                discount_list.append(b)

                num.remove(a)
                num.remove(b)
                break


    result = " ".join(map(str, discount_list))

    print(f"#{tc}", end=" ")
    print(result)


#요약
# 할인가는 정상가의 75%(0.75)
# 정상가는 4의 배수인 정수, 할인가도 모두 정수
#
# 정상가격 20, 80, 100인 경우 할인 가격 15, 60, 75가 되고,
# 출력 더미는 오름차순으로 정렬된 15, 20, 60, 75, 80, 100이 된다.
#
# 할인 가격표만 찾아서 출력하라.

# 풀이
# 정상가는 4를 나눠서 0이고, 현재 리스트에 할인가가 있으면 된다.
# 정상가와 할인가를 모두 리스트에서 삭제
# 탐색할 리스트의 길이가 변했으므로 루프를 탈출한다.
# 리스트에는 아직 숫자가 남아있으므로 리스트가 빌때까지 반복
