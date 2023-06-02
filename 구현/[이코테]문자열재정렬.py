# ----------------------------------------------------------------------------
# [이코테] 문자열 재정렬 (구현, python)
# isdgit() : 숫자이면 참을 반환 isalpha()환환 : 문자열이면 참 반환
# ----------------------------------------------------------------------------
str1 = input()
num = 0
result = []
for i in str1:
    # 숫자이면
    if i.isdigit():
        num += int(i)
    else:
        result.append(i)

# 알파벳 오름차순 정렬
result.sort()

if num != 0:
    result.append(str(num))

print("".join(result))