"""
====================================================================
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하여 후위 표기법을 사용
====================================================================
"""

T = int(input())

for test_case in range(1, T+1):
    postfix = input().split()

    stack = []

    for i in postfix:
        # 종료 포인트(.) 만날 경우
        if i == ".":
            if len(stack) == 1:
                print("#{} {}".format(test_case, stack[0]))
                break
            else:
                print("#{} error".format(test_case))
                break
        # 숫자 만날 경우
        elif i.isdigit() == True:
            stack.append(int(i))
    
        else:       # 연산자 만날 경우
            try:    # 예외 처리(0을 나눌 경우, 숫자를 만나지 않을 경우 등등)
                back_num = stack.pop()
                front_num = stack.pop()

                if i == "+":
                    tmp = front_num + back_num
                    stack.append(tmp)
                elif i == "-":
                    tmp = front_num - back_num
                    stack.append(tmp)
                elif i == "*":
                    tmp = front_num * back_num
                    stack.append(tmp)
                elif i == "/":
                    tmp = front_num // back_num
                    stack.append(tmp)
            except:     # 숫자도 연산자도 아닌경우 
                print("#{} error".format(test_case))
                break
    

"""
오답
채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 10개의 테스트케이스 중 3개가 맞았습니다.)

런타임 에러가 발생하였습니다. 런타임 에러로 전체 혹은 일부 테스트 케이스는 채점이 되지 않을 수 있습니다.
Error Message :
Runtime Error!

========================= try except로 예외 처리 했더니 런타임 에러 사라짐 =========================


여러가지 예외(0을 나눌경우 등등 연산의 오류)를 인식하기 위해 바로 스택에 넣어주면안됨 why??이건 
try except 원리를 알아야 할듯?

"""

