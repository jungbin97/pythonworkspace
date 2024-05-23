# ----------------------------------------------------------------------------
# [baekjoon_2290] LCD Test
# ----------------------------------------------------------------------------
s, n = input().split()
s = int(s)

def lcd(s, num):
    # 배열의 크기 행 2s + 3, 열 2s
    arr = [[" "]*(s+2) for _ in range(2*s+3)]

    if num == "0":
        for i in range(1, s+1):
            arr[0][i] = "-"
            arr[i][0] = "|"
            arr[i][-1] = "|"
            # arr[s+1][i] = "-"
            arr[s+1+i][0] = "|"
            arr[s+1+i][-1] = "|"
            arr[-1][i] = "-"
    elif num == "1":
        for i in range(1, s+1):
            arr[i][-1] = "|"
            arr[s+1+i][-1] = "|"
    elif num == "2":
        for i in range(1, s+1):
            arr[0][i] = "-"
            arr[i][-1] = "|"
            arr[s+1][i] = "-"
            arr[s+1+i][0] = "|"
            arr[-1][i] = "-"
    elif num == "3":
        for i in range(1, s+1):
            arr[0][i] = "-"
            arr[i][-1] = "|"
            arr[s+1][i] = "-"
            arr[s+1+i][-1] = "|"
            arr[-1][i] = "-"
    elif num == "4":
        for i in range(1, s+1):
            arr[i][0] = "|"
            arr[i][-1] = "|"
            arr[s+1][i] = "-"
            arr[s+1+i][-1] = "|"
    elif num == "5":
        for i in range(1, s+1):
            arr[0][i] = "-"
            arr[i][0] = "|"
            arr[s+1][i] = "-"
            arr[s+1+i][-1] = "|"
            arr[-1][i] = "-"
    elif num == "6":
        for i in range(1, s+1):
            arr[0][i] = "-"
            arr[i][0] = "|"
            arr[s+1][i] = "-"
            arr[s+1+i][0] = "|"
            arr[s+1+i][-1] = "|"
            arr[-1][i] = "-"
    elif num == "7":
        for i in range(1, s+1):
            arr[0][i] = "-"
            arr[i][-1] = "|"
            arr[s+1+i][-1] = "|"
    elif num == "8":
        for i in range(1, s+1):
            arr[0][i] = "-"
            arr[i][0] = "|"
            arr[i][-1] = "|"
            arr[s+1][i] = "-"
            arr[s+1+i][0] = "|"
            arr[s+1+i][-1] = "|"
            arr[-1][i] = "-"
    elif num == "9":
        for i in range(1, s+1):
            arr[0][i] = "-"
            arr[i][0] = "|"
            arr[i][-1] = "|"
            arr[s+1][i] = "-"
            arr[s+1+i][-1] = "|"
            arr[-1][i] = "-"
    return arr

result = []
for num in n:
    result.append(lcd(s, num))

for i in range(2*s+3):
    for num_str in result:
        print("".join(num_str[i]), end=" ")
    print()



# 풀이
# 행 : 7 => 2s + 3
# 가로는 있거나 없거나 2가지 경우
# 세로는 왼쪽 양쪽 오른쪽 3가지 경우
# 1 2 3 4 5 6 7 8 9 10
# X 2 2 X 2 2 2 2 2 2

