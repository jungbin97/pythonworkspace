# ----------------------------------------------------------------------------
# [swea_1230] 암호문3 
# ----------------------------------------------------------------------------
for tc in range(1,11):
    # N 암호문 개수
    N = int(input())
    # 암호 뭉치
    password = input().split()
    # M 명령어 개수
    M = int(input())
    # 명령어
    command = input().split()
    
    for i in range(len(command)):
        if command[i] == "I":
            x = int(command[i+1])
            y = int(command[i+2])
            for j in range(y):
                # x번째 위치 뒤에 삽입, insert는 x인덱스 앞에 삽입됨.
                password.insert(x + j, command[i+j+3])
        elif command[i] == "D":
            # x번째 암호문 바로 다음부터 y개 삭제
            x = int(command[i+1])
            y = int(command[i+2])
            for j in range(y):
                password.pop(x+j)
        elif command[i] == "A":
            y = int(command[i+1])
            password.extend(command[i+2:i+2+y])
    
    print(f"#{tc}", end=" ")
    print(*password[:10])

# 풀이
# command 분리하기
# 명령어 별로 수행(list의 pop(), insert(), extend() 메서드에 잘 알고 있어야 한다.)
# "I"명령어는 x번째 암호문 바로 다음에 y개의 암호를 삽입해야한다.
# insert(i, 삽입해야할 것)는 i 인덱스 앞에 삽입하기 때문에, x인덱스에 삽입하면된다.

# "D"명령어는 x번째 암호문 바로 다음부터 y개의 암호를 삭제해야한다.
# pop(i)는 i인덱스 항목을 제거한다.