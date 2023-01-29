T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt_dict = {}
    for i in range(len(str1)):
        cnt_dict[str1[i]] = 0
    
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str2[j] == str1[i]:  # str1 중복을 피해줄 방법??
                cnt += 1
                cnt_dict[str1[i]] = cnt

    print("#{} {}" .format(test_case, max(cnt_dict.values())))
