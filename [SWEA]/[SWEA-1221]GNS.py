# ----------------------------------------------------------------------------
# 딕셔너리 키에 해당하는 value를 기준으로 정렬
# ----------------------------------------------------------------------------

for test_case in range(1, int(input())+1):
    number = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

    tc_numb, n = input().split()
    str = list(input().split())

    # 리스트를 딕셔너리의 value를 기준으로 정렬
    str.sort(key=lambda x : number[x])
    print(tc_numb)
    print(' '.join(str))