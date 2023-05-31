# ----------------------------------------------------------------------------
# [programmers]올바른괄호
# 왼쪽괄호가 나오면 스택에 추가해주고 오른쪽괄호가나오면 pop하면된다.
# 오른쪽괄호가 먼저 나옴(false)
# 순회가 끝났는데 스택 안쪽에 괄호가 남아있는경우(false)
# 모든 괄호가 짝이 맞아서 마지막에 스택이 비게 된 경우(True)
# ----------------------------------------------------------------------------
def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            # 오른쪽 괄호로 시작할경우
            if stack == []:
                  return False
            else:
                stack.pop()
    
    if stack != []: # 순회 끝났는데 괄호가 남아있는 경우
        return False
    return True

print(solution("(())("))