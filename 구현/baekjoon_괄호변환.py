def div_uv(w):
    left = 0
    right = 0
    
    for i in range(len(w)):
        if w[i] == "(":
            left += 1
        else:
            right += 1
        # 균형잡힌 괄호 문자열임(u)
        if left == right:
            return w[:i+1], w[i+1:]

def correct_str(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                break
    # 짝 모두 맞음(올바른 괄호 문자열)
    if cnt == 0:
        return True
    else:
        return False

        
def solution(p):
    answer = ''
    
    # 빈 문자열인 경우 그대로 반환 
    if p == "":
        return ""
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = div_uv(p)
        
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if correct_str(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        return u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        #  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        answer += "("
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        answer += solution(v)
        #  4-3. ')'를 다시 붙입니다. 
        answer += ")"
        #  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        l = list(u)
        del(l[0])
        del(l[-1])
        u = "".join(l)
        
        for i in u:
            if i == "(":
                answer += ")"
            else:
                answer += "("
    return answer
                            

print(solution("()))((()"))