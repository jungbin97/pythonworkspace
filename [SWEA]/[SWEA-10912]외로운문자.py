# ----------------------------------------------------------------------------
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