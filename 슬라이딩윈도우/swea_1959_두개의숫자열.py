# ----------------------------------------------------------------------------
# D2[swea_1959] 두 개의 숫자열 
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    start = 0
    end = 0
    
    result = 0 
    if len(A) < len(B):
        for start in range(len(B)-len(A)+1):
            end = start
            while len(A)-1 > end-start:
                end += 1
            if len(A)-1 == end-start:
                tmp = 0
                B_list = B[start:end+1]
                for i in range(len(A)):
                    tmp += A[i] * B_list[i]
                result = max(result, tmp)
    else:
        for start in range(len(A)-len(B)+1):
            end = start
            while len(B)-1 > end-start:
                end += 1
            if len(B)-1 == end-start:
                tmp = 0
                A_list = A[start:end+1]
                for i in range(len(B)):
                    tmp += A_list[i] * B[i]
                result = max(result, tmp)

    print(f"#{tc} {result}")

# 요약
# N개의 숫자로 구성된 숫자열 A, M개의 숫자로 구성된 숫자열 B
# 더 긴쪽의 양끝을 벗어나면 안되고, 서로 마주보는 숫자를 곱한 뒤 총합의 최대값을 구하시오

# 풀이
# B의 시작 인덱스, 종료 인덱스 정한 후, 이동하면서 최대값을 갱신한다.(배열의 길이가 A로 고정되므로 슬라이딩 윈도우)
