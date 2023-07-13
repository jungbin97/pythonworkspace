# ----------------------------------------------------------------------------
# [baekjoon] 최대공약수와 최소공배수(유클리드호제법, python)
# ---------------------------------------------------------------------------
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
        
a, b = map(int, input().split())

        
gcd = gcd(a, b)
print(gcd)
print(a*b//gcd)

