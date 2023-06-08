# ----------------------------------------------------------------------------
# [이코테] 문자열 압축(구현, python)
# ----------------------------------------------------------------------------
def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        compressed = 0
        temp = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if temp == s[j:j+i]:
                cnt += 1
            else:   # temp == s[j:j+i]와 다를 때
                temp_n = len(str(cnt))+i if cnt>1 else i
                compressed += temp_n
                temp = s[j:j+i]
                print(i,j,j+i,temp)
                cnt = 1
        
        if cnt > 1:
            compressed += len(str(cnt))+i
        else:
            compressed += len(temp)
        answer = min(answer, compressed)

    return answer

print(solution("aabbaccc"))