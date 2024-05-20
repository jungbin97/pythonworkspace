# ----------------------------------------------------------------------------
# [baekjoon_3568] iSharp 
# ----------------------------------------------------------------------------
string = input().replace(",", "").replace(";", "").split()

# 기본 변수형
default_variable = string[0]

variable = string[1:]
# print(variable)
result = []
for i in range(len(variable)):
    # 변수명
    varibale_name = ""
    variable_suffix = ""
    for char in variable[i]:
        if char.isalpha():
            varibale_name = varibale_name + char
        else:
            variable_suffix = variable_suffix + char
            
    result.append(default_variable + variable_suffix[::-1].replace("][", "[]") + " " + varibale_name +";")

print("\n".join(result))