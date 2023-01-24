#그리디
import sys
import time

start = time.time()

n = int(sys.stdin.readline())

cnt = 0

while 1:
    if n%5 == 0:    #5의 배수이면
        cnt += (n//5)
        print(cnt)
        break
    n -= 3
    cnt += 1
    if n<0:
        print(-1)
        break
print(time.time() - start)      

#다이나믹 프로그래밍(DP)
'''
N = int(sys.stdin.readline())
cnt = [-1 for _ in range(N+1)]
cnt[3] = 1
if 5 <= N:
    cnt[5] = 1

for i in range(6, N+1):
    a, b = cnt[i-3], cnt[i-5]
    if a != -1 or b != -1:
        if a != -1 and b != -1:
            cnt[i] = min(a, b) + 1
        else:
            cnt[i] = max(a, b) + 1
print(cnt[-1])

  
'''