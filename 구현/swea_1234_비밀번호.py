# ----------------------------------------------------------------------------
# [swea_1234] 비밀번호
# ----------------------------------------------------------------------------
for tc in range(1, 11):
    n, nums = input().split()
    n = int(n)
    nums = list(map(str, nums))

    stack = []
    for i in nums:
        # 스택이 비어있다면 현재 원소 추가
        if len(stack) == 0:
            stack.append(i)
        else:
            # 스택 최상단과 같으면 pop()
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    
    result = "".join(stack)
    print(f"#{tc} {result}")


# 요약
# 같은 번호가 붙어있는 쌍을 소거하고 남은 번호를 비밀번호로 만든다.
# 번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거 가능

# 풀이
# stack을 이용해서 풀자
# 1. 스택에 아무것도 들어있지 않으면 len(stack) == 0, 스택에 추가
# 2. 스택의 최상단과 같지 않으면 현재 원소 스택에 추가
# 3. 스택의 최상단 원소가 같으면 pop()