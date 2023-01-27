T = int(input())

for test_case in range(1, T+1):

    str1 = input() # 매칭 문자열
    str2 = input() # 전체 문자열

    if str1 in str2:
        print("#%d %d" %(test_case, 1))
    else:
        print("#%d %d" %(test_case, 0))