# ----------------------------------------------------------------------------
# 1. 정렬 후 stack 넣어 중복되면 제거한다.
# ----------------------------------------------------------------------------
for test_case in range(1, int(input())+1):
    str = list(input())
    str.sort()
    stack = []

    for s in str:
        if s not in stack:
            stack.append(s)
        else:
            stack.remove(s)
            
    if len(stack) != 0:
        print("#{} {}".format(test_case, "".join(stack)))
    else:
        print("#{} {}".format(test_case, "Good"))