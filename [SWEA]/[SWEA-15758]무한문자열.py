# ------------------------------------------------------------------
# 1. 길이를 맞게 맞춰준후 비교함
# ------------------------------------------------------------------

for test_case in range(1, int(input())+1):
    strs = list(input().split())

    def infinite(a, b):
        ss = a * len(b)
        tt = b * len(a)
   
        if ss == tt:
            print("#{} yes".format(test_case))
        else:
            print("#{} no".format(test_case))

    infinite(strs[0], strs[1])