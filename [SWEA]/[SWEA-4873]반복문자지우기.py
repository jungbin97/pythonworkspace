T = int(input())

for test_case in range(1, T+1):
    repeat_str = input()
    stack = []
    
    for i in repeat_str:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print("#%d %d"%(test_case, len(stack)))