# ------------------------------------------------------
#  [프로그래머스] N으로 표현하기 (DP)
# ------------------------------------------------------

def solution(N, number):
    if N == number:
        return 1
    
    # SET * 8 초기화(n을 해당개수만큼 사용해 만들수 있는 수(N의 개수 8보다 크면 return -1))
    s = [set() for x in range(8)]

    # 각 set마다 기본수 N * i 수 초기화(5, 55, 555 등등)
    for i,x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    for i in range(1, 8):
        for j  in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:    # 0으로 나누는 것은 불가능
                        s[i].add(op1 // op2)
                    
        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer


print(solution(5, 12))