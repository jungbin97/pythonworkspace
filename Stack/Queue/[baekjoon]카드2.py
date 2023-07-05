# ----------------------------------------------------------------------------
# [baekjoon] 카드2 (queue, python)
# 홀수면 버리고, 짝수면 큐에서 뺀후 다시 추가 (x)
# 버리고, 밑으로 옮기고 반복(짝수 홀수 기준이 아님)
# ----------------------------------------------------------------------------
import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

q = deque()
cnt = 1
# 큐 초기화
for i in range(1, N+1):
    q.append(i)

while len(q)>1:
    card = q.popleft()
    # 홀수 일경우
    if cnt%2 == 1:
        cnt+=1
        continue
    # 짝수일경우
    else:
        q.append(card)
        cnt+=1

print(q.pop())