# ----------------------------------------------------------------------------
# [swea_1228] 암호문1
# ----------------------------------------------------------------------------
for tc in range(1, 11):
    # 암호문 길이 N
    N = int(input())
    password = input().split()
    # 명령어 개수 M
    M = int(input())
    command = input().split()

    for i in range(len(command)):
        if command[i] == "I":
            x = int(command[i+1])
            y = int(command[i+2])
            for j in range(y):
                password.insert(x+j, command[i+j+3])

    print(f"#{tc}", end=" ")
    print(*password[:10])