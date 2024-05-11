# ----------------------------------------------------------------------------
# [baekjoon_2581] 소수
# ----------------------------------------------------------------------------
import sys
import math
input = sys.stdin.readline

m = int(input())
n = int(input())

prime = []
a = [True]* (n+1)

for i in range(2, n+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

new_prime = []
for i in prime:
    if i < m:
        continue
    else: 
        new_prime.append(i)

if len(new_prime):
    print(sum(new_prime))
    print(min(new_prime))
else:
    print(-1)