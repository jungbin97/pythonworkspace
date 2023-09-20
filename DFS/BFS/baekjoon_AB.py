# ----------------------------------------------------------------------------
# [baekjoon_16953] A -> B 
# ----------------------------------------------------------------------------
from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def solution(a,b):
    q = deque([(a, 1)])

    while q:
        a, cnt = q.popleft()
        if a==b:
            print(cnt)
            return
        
        if a <= b:
            q.append((a*2, cnt+1))
            q.append((a*10+1, cnt+1))
    print(-1)

solution(a,b)