# ----------------------------------------------------------------------------
# [baekjoon_15721] 번데기 (구현, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

A = int(input())
T = int(input())
target = int(input())   # 0 : 뻔, 1 : 데기

bun = 0
degi = 0
count = 2

while True:
    # 뻔 데기 뻔 데기
    for i in range(4):
        if i%2==0:
            bun+= 1
            if bun==T and target == 0:
                print((bun+degi-1)%A)
                exit(0)
        else:
            degi+= 1
            if bun==T and target == 1:
                print((bun+degi-1)%A)
                exit(0)

    for i in range(count):
        bun += 1
        if bun==T and target == 0:
            print((bun+degi-1)%A)
            exit(0)
    
    for i in range(count):
        degi += 1
        if degi==T and target == 1:
            print((bun+degi-1)%A)
            exit(0)
    count+= 1