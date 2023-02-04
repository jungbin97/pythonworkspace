def bracket_test(input_str):
    stack = []
    result = 1
    for i in input_str:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}' or i == ')':
            if len(stack) == 0:
                result = 0
                break
            elif i == '}' and stack.pop() == '(':
                result = 0
                break
            elif i == ')' and stack.pop() == '}':
                result = 0
                break

    if len(stack):
        result = 0
    return result

T = int(input())

for test_case in range(1, T+1):
    input_str = input()

    print("#{} {}".format(test_case, bracket_test(input_str)))
    