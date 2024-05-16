# ----------------------------------------------------------------------------
# D3[swea_11856] 반반
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    string = input()

    string_dict = {}
    for i in string:
        if i in string_dict:
            string_dict[i] += 1
        else:
            string_dict[i] = 1

    value_set = set(string_dict.values())

    if len(value_set) == 1 and len(string_dict.keys()) == 2:
        print(f"#{tc} {'Yes'}")
    else:
        print(f"#{tc} {'No'}")
