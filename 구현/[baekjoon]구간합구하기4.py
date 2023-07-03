import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
sumList = [0] * (N+1)

for i in range(N):
    sumList[i+1] = sumList[i] + A[i]
    
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sumList[j]-sumList[i-1])