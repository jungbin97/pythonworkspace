# ----------------------------------------------------------------------------
# [baekjoon_2784] 가로 세로 퍼즐
# ----------------------------------------------------------------------------
import sys
import copy
from itertools import permutations
input = sys.stdin.readline

puzzle = [input().rstrip() for _ in range(6)]

def check(board):
    visited = [False] * 6
    count = 0 
    for i in range(3):
        # 가로줄 확인
        for j in range(6):
            if not visited[j] and board[i] == puzzle[j]:
                visited[j] = True
                count += 1
                break
        temp = "".join(board[j][i] for j in range(3))
        # 세로줄 생성
        for j in range(6):
            if not visited[j] and temp == puzzle[j]:
                visited[j] = True
                count += 1
                break
    
    return count == 6


# 모든 3개의 단어 조합
found = False
for i in range(6):
    for j in range(6):
        if i == j:
            continue
        for k in range(6):
            if i == k or j == k:
                continue 
            board = [puzzle[i], puzzle[j], puzzle[k]]
            if check(board):
                for line in board:
                    print(line)
                found = True
                break
        if found:
            break
    if found:
        break

if not found:
    print(0)



# 요약
# DAR
# ANA
# RAD
# 주어진 6개 단어를 3X3 퍼줄에 출력해야한다.
# 가능하면 퍼즐모양을 출력하고, 불가능하면 0을 출력한다.


# # 풀이
# 완전탐색으로 펴줄모양을 만든다음 6개단어가 모두 존재하는지 체크합니다.
# 6개의 단어를 순서가 존재하도록3개 뽑아야합니다. 6P3 => 120가지 경우의 수
# 3개의 행을 추출하여 선택되지 않은 행이 열에 전부 존재하는지 확인합니다.
