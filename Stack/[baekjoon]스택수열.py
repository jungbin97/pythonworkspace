import sys
N = int(sys.stdin.readline().rstrip())

stack = []
current = 1
# 정답 출력 리스트
answer = []
flag = 0
for i in range(N):
    num = int(sys.stdin.readline().rstrip())  # pop할 숫자 입력받음
    while current <= num:   # 작거나 같으면 push
        stack.append(current)
        answer.append("+")
        current += 1

    if stack[-1] == num:
        answer.append("-")
        stack.pop()
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)