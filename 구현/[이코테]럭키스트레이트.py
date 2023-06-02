# ----------------------------------------------------------------------------
# [이코테] 럭키스트레이트 (구현, python)
# ----------------------------------------------------------------------------

# str = input()
# front  = 0
# back = 0
# for i in range(len(str)):
#     if i < len(str)//2:
#         front += int(str[i])
#     else:
#         back += int(str[i])

# if front == back:
#     print("LUCKY")
# else:
#     print("READY")

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

str = input()
length = len(str)
summary = 0

for i in range(length):
    if i < length//2:
        summary += int(str[i])
    else:
        summary -= int(str[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")