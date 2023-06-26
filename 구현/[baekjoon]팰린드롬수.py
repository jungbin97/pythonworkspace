import sys

while True:
    str = sys.stdin.readline().strip()
    length = len(str)
    # 홀수일경우
    if str == '0':
        break
    elif str == str[::-1]:
        print("yes")
    else:
        print("no")