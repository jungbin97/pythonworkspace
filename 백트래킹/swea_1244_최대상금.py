# ----------------------------------------------------------------------------
# D3[swea_1244] 최대 상금
# ----------------------------------------------------------------------------
def dfs(n):
    global answer
    # 탈출조건 n의 깊이가 최대 교환횟수를 도달할경우 모든 경우의수 추출한 것.
    if n == N:
        answer = max(answer, int("".join(map(str, nums))))
        return
    
    # 6C2 조합
    for i in range(0, L-1):
        for j in range(i+1, L):
            nums[i], nums[j] = nums[j], nums[i]
            check = int("".join(map(str, nums)))
            if (n, check) not in visited:
                dfs(n+1)
                visited.append((n, check))
            # 복구
            nums[i], nums[j] = nums[j], nums[i]
            
for tc in range(1, int(input())+1):
    nums, N = map(str, input().split())
    nums = list(int(i) for i in nums)
    N = int(N)
    answer = 0
    
    L = len(nums)
    visited = []
    dfs(0)

    print(f"#{tc} {answer}")


# 요약
# 정해진 숫자 만큼 교환했을 경우 가장 큰 금액을 계산 하라.(교환횟수를 전부 사용해야한다.)

# 풀이
# 6C2 = 15 => 두수 선택해서 교환
# 15^10 이다.