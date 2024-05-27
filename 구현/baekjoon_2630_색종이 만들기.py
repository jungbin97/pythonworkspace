# ----------------------------------------------------------------------------
# [baekjoon_2630] 색종이 만들기
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

blue_cnt = 0
white_cnt = 0

# 행 , 열
def check(r_start, r_end, c_start, c_end):
    global blue_cnt, white_cnt
    tmp = 0
    same_flag = True 

    # 잘라진 종이가 모두 같은 색인지 체크, 같으면 탈출 +1
    for i in range(r_start, r_end):
        for j in range(c_start, c_end):
            if i == r_start and j == c_start:
                tmp = graph[i][j]
                
            if tmp != graph[i][j]:
                same_flag = False 
                break 
        if not same_flag:
            break
            
    # 같지않다면 or 더이상 자를 수 없다면?
    if not same_flag:
        mid_r = int((r_start + r_end)/2)
        mid_c = int((c_start + c_end)/2)
        # 1사분면
        check(r_start, mid_r, c_start, mid_c)
        # 2사분면
        check(r_start, mid_r, mid_c, c_end)
        # 3사분면
        check(mid_r, r_end, c_start, mid_c)
        # 4사분면
        check(mid_r, r_end, mid_c, c_end)
    else:
        # 무사히 끝나면 전부 같은것?
        if tmp == 1:
            blue_cnt += 1
        elif tmp == 0:
            white_cnt += 1


check(0, N, 0, N)
print(white_cnt)
print(blue_cnt)


# 요약
# 전체 종이 크기가 1 <= N <= 7 이라면
# 전체 종이가 모두 같은 색이 아니면 4등분함.(4가지 모두 같은 크기로)

# 잘라진 종이가 모두 하얀색 또는 파랑색 또는 더이상 자를수 없을때까지 반복


# 한얀색 색종이의 개수와 파란색 색종이 개수를 출력하라.


# 풀이
# 전부 같은지 체크
# 같지 않으면 n/2 만큼 모두 짤라서 4사분면 모두 체크
# 모두 같으면 +1