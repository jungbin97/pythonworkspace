# ----------------------------------------------------------------------------
# [swea_1229] 암호문2
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
            for j in range(0, y):
                password.insert(x+j, command[i+j+3])
        elif command[i] == "D":
            x = int(command[i+1])
            y = int(command[i+2])
            for j in range(0, y):
                del password[x]

    print(f"#{tc}", end=" ")
    print(*password[:10])