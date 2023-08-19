# ----------------------------------------------------------------------------
# [baekjoon_15721] 번데기 (구현, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

A = int(input())
T = int(input())
target = int(input())   # 0 : 뻔, 1 : 데기

bundegi = []
bun, degi = 0

turn = 0
while True:
    prevbundegiNum = bun
    turn += 1
    for _ in range(2):
        bundegi.append((bun, 0))
        bun += 1
        bundegi.append((degi, 1))
        degi += 1
    for _ in range(turn + 1):
        bundegi.append((bun, 0))
        bun += 1
    for _ in range(turn + 1):
        bundegi.append((degi, 1))
        degi += 1
    if prevbundegiNum < T <= bun:
        print(bundegi.index((T, target)) % A)